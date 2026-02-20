# main.py
import os
import sys

from PySide6.QtCore import QUrl
from PySide6.QtCore import Qt, Signal, QPoint
from PySide6.QtGui import QAction, QDesktopServices
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog,
    QMessageBox, QMenu, QFrame, QGroupBox
)

from ui.file_card import Ui_file_card
from ui.file_selection_screen import Ui_file_selection_screen
from ui.main_window import Ui_MainWindow
from ui.search_screen import Ui_GroupBox


class FileCard(QFrame):
    """Виджет карточки файла"""

    selected_changed = Signal(object, bool)  # сигнал об изменении выделения (карточка, выделена)
    double_clicked = Signal(object)  # сигнал двойного клика

    def __init__(self, file_path: str, parent=None):
        super().__init__(parent)
        self.ui = Ui_file_card()
        self.ui.setupUi(self)

        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        self.is_selected = False

        # Настройка внешнего вида
        self.ui.file_name.setText(self.file_name)
        self.ui.select_file.clicked.connect(self.toggle_selection)
        self.ui.select_file.setVisible(False)  # изначально чекбокс скрыт
        self.ui.select_file.setChecked(False)

        # Подключаем контекстное меню
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

        # Для обработки двойного клика
        self.ui.file_icon.installEventFilter(self)
        self.ui.file_name.installEventFilter(self)

    def eventFilter(self, obj, event):
        """Фильтр событий для обработки двойного клика"""
        if event.type() == event.Type.MouseButtonDblClick:
            if event.button() == Qt.LeftButton:
                self.double_clicked.emit(self)
                return True
        return super().eventFilter(obj, event)

    def mouseDoubleClickEvent(self, event):
        """Обработка двойного клика по карточке"""
        if event.button() == Qt.LeftButton:
            self.double_clicked.emit(self)
        super().mouseDoubleClickEvent(event)

    def show_context_menu(self, pos: QPoint):
        """Показ контекстного меню"""
        menu = QMenu(self)

        open_action = QAction("Открыть", self)
        open_action.triggered.connect(lambda: self.double_clicked.emit(self))

        select_action = QAction("Выбрать", self)
        select_action.triggered.connect(self.select_from_menu)

        delete_action = QAction("Удалить", self)
        delete_action.triggered.connect(self.delete_card)

        menu.addAction(open_action)
        menu.addAction(select_action)
        menu.addAction(delete_action)

        menu.exec(self.mapToGlobal(pos))

    def select_from_menu(self):
        """Выбор карточки через контекстное меню"""
        self.set_selected(True)

    def set_selected(self, selected: bool):
        """Установка состояния выделения карточки"""
        if self.is_selected == selected:
            return

        self.is_selected = selected
        self.ui.select_file.setChecked(selected)
        self.ui.select_file.setVisible(True)  # показываем чекбокс

        # Изменяем внешний вид
        if selected:
            self.setStyleSheet("""
                QFrame {
                    background-color: rgba(155, 255, 255, 30);
                    border: 1px solid white;
                }
            """)
        else:
            self.setStyleSheet("""
                QFrame {
                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                                      stop:0 rgba(50, 50, 50, 255), 
                                                      stop:1 rgba(70, 70, 70, 255));
                }
            """)

        self.selected_changed.emit(self, selected)

    def toggle_selection(self):
        """Переключение выделения"""
        self.set_selected(not self.is_selected)

    def hide_checkbox(self):
        self.ui.select_file.setVisible(False)

    def delete_card(self):
        """Удаление карточки"""
        self.deleteLater()


class FileSelectionScreen(QGroupBox):
    """Экран выбора файлов"""

    next_clicked = Signal()  # сигнал для перехода на следующий экран

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_file_selection_screen()
        self.ui.setupUi(self)

        # Скрываем кнопки выбора по умолчанию
        self.ui.select_all_button.hide()
        self.ui.selection_cancel_button.hide()
        self.ui.delete_button.hide()

        # Список карточек файлов
        self.file_cards = []

        # Подключаем сигналы
        self.ui.add_button.clicked.connect(self.add_files)
        self.ui.select_all_button.clicked.connect(self.toggle_select_all)
        self.ui.selection_cancel_button.clicked.connect(self.cancel_selection)
        self.ui.delete_button.clicked.connect(self.delete_selected)
        self.ui.button_next.clicked.connect(self.next_clicked.emit)

        # Переменная для отслеживания состояния "выбрать все"
        self.select_all_state = False

    def add_files(self):
        """Открыть диалог выбора PDF файлов"""
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Выберите PDF файлы",
            "",
            "PDF Files (*.pdf)"
        )

        for file_path in files:
            self.add_file_card(file_path)

    def add_file_card(self, file_path: str):
        """Добавить карточку файла"""
        # Проверяем, нет ли уже такого файла
        for card in self.file_cards:
            if card.file_path == file_path:
                return

        card = FileCard(file_path)
        card.selected_changed.connect(self.on_card_selection_changed)
        card.double_clicked.connect(self.open_file)

        # Добавляем в grid
        row = len(self.file_cards) // 4  # 4 карточки в ряд
        col = len(self.file_cards) % 4
        self.ui.files_grid_layout.addWidget(card, row, col, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        self.file_cards.append(card)

    def on_card_selection_changed(self, card: FileCard, selected: bool):
        """Обработка изменения выделения карточки"""
        selected_count = self.get_selected_count()

        if selected_count > 0:
            # Показываем кнопки выбора
            self.ui.select_all_button.show()
            self.ui.selection_cancel_button.show()
            self.ui.delete_button.show()

            # Обновляем состояние "выбрать все"
            all_selected = selected_count == len(self.file_cards)
            self.ui.select_all_button.setChecked(all_selected)
            self.select_all_state = all_selected
        else:
            # Скрываем кнопки
            self.ui.select_all_button.hide()
            self.ui.selection_cancel_button.hide()
            self.ui.delete_button.hide()
            card.hide_checkbox()

    def get_selected_count(self) -> int:
        """Получить количество выделенных карточек"""
        return sum(1 for card in self.file_cards if card.is_selected)

    def toggle_select_all(self, checked: bool):
        """Обработка нажатия на "Выбрать все" """
        if checked:
            # Выделяем все
            for card in self.file_cards:
                card.set_selected(True)
        else:
            # Снимаем выделение со всех (но чекбоксы остаются видимыми)
            for card in self.file_cards:
                if card.is_selected:
                    card.set_selected(False)
                card.hide_checkbox()

    def cancel_selection(self):
        """Отмена выделения"""
        for card in self.file_cards:
            if card.is_selected:
                card.set_selected(False)

    def delete_selected(self):
        """Удаление выделенных карточек"""
        # Подтверждение удаления
        reply = QMessageBox.question(
            self,
            "Подтверждение",
            "Удалить выбранные файлы из списка?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            selected_cards = [card for card in self.file_cards if card.is_selected]
            for card in selected_cards:
                self.file_cards.remove(card)
                card.delete_card()

    def open_file(self, card: FileCard):
        """Открыть файл"""
        QDesktopServices.openUrl(QUrl.fromLocalFile(card.file_path))


class SearchScreen(QGroupBox):
    """Экран поиска"""

    back_clicked = Signal()  # сигнал для возврата

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_GroupBox()
        self.ui.setupUi(self)

        # Подключаем сигналы
        self.ui.return_button.clicked.connect(self.back_clicked.emit)


class MainWindow(QMainWindow):
    """Главное окно приложения"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("PDF Manager")

        # Создаем экраны
        self.file_selection_screen = FileSelectionScreen()
        self.search_screen = SearchScreen()

        # Подключаем сигналы
        self.file_selection_screen.next_clicked.connect(self.show_search_screen)
        self.search_screen.back_clicked.connect(self.show_file_selection_screen)

        # Показываем первый экран
        self.show_file_selection_screen()

    def show_file_selection_screen(self):
        """Показать экран выбора файлов"""
        # Очищаем центральный виджет
        self.clear_central_widget()
        # Устанавливаем экран выбора файлов
        self.ui.centralwidget.layout().addWidget(self.file_selection_screen)

    def show_search_screen(self):
        """Показать экран поиска"""
        # Очищаем центральный виджет
        self.clear_central_widget()
        # Устанавливаем экран поиска
        self.ui.centralwidget.layout().addWidget(self.search_screen)

    def clear_central_widget(self):
        """Очистить центральный виджет"""
        layout = self.ui.centralwidget.layout()
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()


def main():
    app = QApplication(sys.argv)

    # Устанавливаем тему (опционально)
    app.setStyle("Fusion")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()