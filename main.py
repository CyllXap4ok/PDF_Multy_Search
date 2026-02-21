import os
import sys

from PySide6.QtCore import QUrl, QEasingCurve, QVariantAnimation
from PySide6.QtCore import Qt, Signal, QPoint
from PySide6.QtGui import QAction, QDesktopServices
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog,
    QMessageBox, QMenu, QFrame, QGroupBox, QStackedWidget, QWidget
)

from ui.file_card import Ui_file_card
from ui.file_selection_screen import Ui_file_selection_screen
from ui.flow_layout import FlowLayout
from ui.main_window import Ui_MainWindow
from ui.search_screen import Ui_GroupBox


class FileCard(QFrame):

    selection_changed_signal = Signal(object, bool)
    double_clicked_signal = Signal(object)
    delete_signal = Signal(object)

    def __init__(self, file_path, parent=None):
        #Дефолтная привязка
        super().__init__(parent)
        self.ui = Ui_file_card()
        self.ui.setupUi(self)

        #Переменные пути и имени файла
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)

        #Переменные состояния карточки
        self.selectable = False
        self.is_selected = False

        #Установка названия файла
        self.ui.file_name.setText(self.file_name)

        #Настройка контекстного меню
        self.menu = QMenu(self)
        open_action = QAction("Открыть", self)
        open_action.triggered.connect(lambda: self.double_clicked_signal.emit(self.file_path))

        select_action = QAction("Выбрать", self)
        select_action.triggered.connect(self.select_from_menu)

        delete_action = QAction("Удалить", self)
        delete_action.triggered.connect(lambda: self.delete_signal.emit(self))

        self.menu.addAction(open_action)
        self.menu.addAction(select_action)
        self.menu.addAction(delete_action)

        #Установка контекстного меню
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, pos: QPoint):
        if not self.selectable: self.menu.exec(self.mapToGlobal(pos))

    def select_from_menu(self):
        self.set_selectability(True)
        self.change_selection()

    def set_selectability(self, selectable: bool):
        if not selectable: self.set_selection(selectable)
        self.selectable = selectable

    def set_selection(self, selected: bool):
        if self.is_selected == selected or not self.selectable == True: return;

        self.is_selected = selected

        if selected:
            self.setStyleSheet("""
                QFrame#file_card {
                    background-color: rgba(155, 255, 252, 30);
                    border: 1px solid white;
                    border-radius: 10px;
                }    
            """)
        else:
            self.setStyleSheet("""
                QFrame#file_card {
                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(50, 50, 50, 255), stop:1 rgba(70, 70, 70, 255));
                    border: none;
                    border-radius: 10px;
                }
                
                QFrame#file_card:hover {
                    background-color: rgba(155, 255, 252, 30);
                }
            """)

        self.selection_changed_signal.emit(self, selected)

    def change_selection(self):
        self.set_selection(not self.is_selected)

    def mousePressEvent(self, event):
        if self.selectable and event.button() == Qt.MouseButton.LeftButton:
            self.change_selection()
        super().mousePressEvent(event)

    def mouseDoubleClickEvent(self, event):
        if not self.selectable and event.button() == Qt.MouseButton.LeftButton:
            self.double_clicked_signal.emit(self.file_path)
        super().mouseDoubleClickEvent(event)

    def get_file_path(self):
        return self.file_path

    def delete_card(self):
        self.deleteLater()


class FileSelectionScreen(QGroupBox):

    next_clicked = Signal(object, list[str])

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_file_selection_screen()
        self.ui.setupUi(self)

        self.ui.select_all_button.hide()
        self.ui.selection_cancel_button.hide()
        self.ui.delete_button.hide()
        self.ui.button_next.setEnabled(False)

        self.file_cards = []

        self.ui.add_button.clicked.connect(self.add_files)
        self.ui.select_all_button.clicked.connect(self.toggle_select_all)
        self.ui.selection_cancel_button.clicked.connect(self.cancel_selection)
        self.ui.delete_button.clicked.connect(self.delete_selected)
        self.ui.button_next.clicked.connect(lambda: self.next_clicked.emit([card.get_file_path() for card in self.file_cards]))

        self.is_selection_state = False

        # Создаем новый контейнер с FlowLayout и устанавливаем его в scroll area
        self.scroll_container = QWidget()
        self.files_grid = FlowLayout(self.scroll_container)
        self.ui.scrollArea.setWidget(self.scroll_container)

    def add_files(self):
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Выберите PDF файлы",
            "",
            "PDF Files (*.pdf)"
        )

        for file_path in files:
            self.add_file_card(file_path)

        files_count = len(self.file_cards)
        if files_count > 0:
            self.ui.button_next.setEnabled(True)

        self.ui.label.setText("Добавлено файлов - " + str(files_count))

    def add_file_card(self, file_path: str):
        for card in self.file_cards:
            if card.file_path == file_path:
                return

        card = FileCard(file_path)
        card.selection_changed_signal.connect(self.on_card_selection_changed)
        card.double_clicked_signal.connect(open_file)
        card.delete_signal.connect(lambda: self.delete_card(card))

        # Добавляем карточку в flow_layout
        self.files_grid.addWidget(card)
        self.file_cards.append(card)

        # Обновляем счетчик
        self.ui.label.setText("Добавлено файлов - " + str(len(self.file_cards)))

    def delete_card(self, card: FileCard):
        reply = QMessageBox.question(
            self,
            "Подтверждение",
            "Удалить выбранный файл из списка?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.file_cards.remove(card)
            self.files_grid.removeWidget(card)
            card.delete_card()
            self.ui.label.setText("Добавлено файлов - " + str(len(self.file_cards)))

            if len(self.file_cards) == 0: self.ui.button_next.setEnabled(False)

    def delete_selected(self):
        reply = QMessageBox.question(
            self,
            "Подтверждение",
            "Удалить выбранные файлы из списка?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            selected_cards = [card for card in self.file_cards if card.is_selected]
            for card in selected_cards:
                self.file_cards.remove(card)
                self.files_grid.removeWidget(card)
                card.delete_card()

            self.set_selection_state(False)
            if len(self.file_cards) == 0: self.ui.button_next.setEnabled(False)
            self.ui.label.setText("Добавлено файлов - " + str(len(self.file_cards)))

    def on_card_selection_changed(self):
        if not self.is_selection_state:
            self.set_selection_state(True)

        selected_count = self.get_selected_count()

        if selected_count > 0:
            all_selected = selected_count == len(self.file_cards)
            self.ui.select_all_button.setChecked(all_selected)
            self.ui.delete_button.setEnabled(True)
        else:
            self.ui.delete_button.setEnabled(False)
            self.ui.select_all_button.setChecked(False)

    def set_selection_state(self, enable_selection: bool):
        self.ui.select_all_button.setVisible(enable_selection)
        self.ui.selection_cancel_button.setVisible(enable_selection)
        self.ui.delete_button.setVisible(enable_selection)

        self.ui.add_button.setEnabled(not enable_selection)
        self.ui.button_next.setEnabled(not enable_selection)

        for card in self.file_cards:
            if not enable_selection: card.set_selection(False)
            card.set_selectability(enable_selection)

        self.is_selection_state = enable_selection

    def get_selected_count(self) -> int:
        return sum(1 for card in self.file_cards if card.is_selected)

    def toggle_select_all(self, checked: bool):
        if checked:
            for card in self.file_cards:
                card.set_selection(True)
        else:
            for card in self.file_cards:
                if card.is_selected:
                    card.set_selection(False)

    def cancel_selection(self):
        self.set_selection_state(False)


class SearchScreen(QGroupBox):

    back_clicked = Signal()  # сигнал для возврата

    def __init__(self, file_paths: list[str]=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_GroupBox()
        self.ui.setupUi(self)
        self.ui.return_button.clicked.connect(self.back_clicked.emit)

        if file_paths is None: self.file_paths = []
        else: self.file_paths = file_paths

    def search(self):
        """TODO()"""

    def show_results(self):
        """TODO()"""

    def set_file_paths(self, file_paths: list[str]):
        """TODO()"""


class AnimatedStackedWidget(QStackedWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.animation_duration = 300  # мс
        self.animation_direction = 'left'  # 'left' или 'right'
        self.current_widget = None
        self.next_widget = None

        # Создаем анимацию
        self.animation = QVariantAnimation()
        self.animation.valueChanged.connect(self.animate_step)
        self.animation.finished.connect(self.animation_finished)

    def set_duration(self, ms):
        self.animation_duration = ms

    def slide_in_left(self, next_widget):
        self.animation_direction = 'left'
        self.start_animation(next_widget)

    def slide_in_right(self, next_widget):
        self.animation_direction = 'right'
        self.start_animation(next_widget)

    def start_animation(self, next_widget):
        self.current_widget = self.currentWidget()
        self.next_widget = next_widget

        if not self.current_widget or self.current_widget == next_widget:
            return

        # Показываем следующий виджет, но делаем его невидимым
        self.next_widget.setGeometry(self.current_widget.geometry())
        self.next_widget.show()
        self.next_widget.lower()

        # Настраиваем анимацию
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.setDuration(self.animation_duration)
        self.animation.setEasingCurve(QEasingCurve.Type.OutCubic)

        self.animation.start()

    def animate_step(self, value):
        if not self.current_widget or not self.next_widget:
            return

        width = self.current_widget.width()

        if self.animation_direction == 'left':
            # Текущий виджет уходит влево
            self.current_widget.move(int(-width * value), 0)
            # Следующий виджет появляется справа
            self.next_widget.move(int(width * (1 - value)), 0)
        else:
            # Текущий виджет уходит вправо
            self.current_widget.move(int(width * value), 0)
            # Следующий виджет появляется слева
            self.next_widget.move(int(-width * (1 - value)), 0)

        self.next_widget.raise_()

    def animation_finished(self):
        # Завершаем анимацию
        self.current_widget.hide()
        self.current_widget.move(0, 0)
        self.setCurrentWidget(self.next_widget)
        self.current_widget = None
        self.next_widget = None


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("PDF Manager")

        # Создаем анимированный stacked widget
        self.stacked_widget = AnimatedStackedWidget()
        self.ui.centralwidget.layout().addWidget(self.stacked_widget)

        # Создаем и добавляем экраны
        self.file_selection_screen = FileSelectionScreen()
        self.search_screen = SearchScreen()

        self.stacked_widget.addWidget(self.file_selection_screen)
        self.stacked_widget.addWidget(self.search_screen)

        # Подключаем сигналы с анимацией
        self.file_selection_screen.next_clicked.connect(self.switch_to_search_screen)
        self.search_screen.back_clicked.connect(self.switch_to_file_selection_screen)

        # Показываем первый экран
        self.stacked_widget.setCurrentWidget(self.file_selection_screen)

    def switch_to_search_screen(self, file_paths: list[str]):
        self.search_screen.set_file_paths(file_paths)
        self.stacked_widget.slide_in_left(self.search_screen)

    def switch_to_file_selection_screen(self):
        self.stacked_widget.slide_in_right(self.file_selection_screen)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


def open_file(file_path: str):
    QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))


if __name__ == "__main__":
    main()