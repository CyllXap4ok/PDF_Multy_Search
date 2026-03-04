import sys

from PySide6.QtCore import QEasingCurve, QVariantAnimation
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QStackedWidget
)

from ui.ui_main_window import Ui_MainWindow
from view_model.file_selection_screen import FileSelectionScreen
from view_model.search_screen import SearchScreen


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
        self.setWindowTitle("DocSearch")

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


if __name__ == "__main__":
    main()