from PySide6.QtCore import QPoint, QRect, QSize, Qt
from PySide6.QtWidgets import QLayout


class FlowLayout(QLayout):
    def __init__(self, parent=None, margin=0, spacing=5):
        super().__init__(parent)

        if parent is not None:
            self.setContentsMargins(margin, margin, margin, margin)

        self.setSpacing(spacing)

        self.item_list = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        self.item_list.append(item)

    def count(self):
        return len(self.item_list)

    def itemAt(self, index):
        if 0 <= index < len(self.item_list):
            return self.item_list[index]
        return None

    def takeAt(self, index):
        if 0 <= index < len(self.item_list):
            return self.item_list.pop(index)
        return None

    def expandingDirections(self):
        return Qt.Orientation(0)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self.do_layout(QRect(0, 0, width, 0), True)
        return height

    def setGeometry(self, rect):
        super().setGeometry(rect)
        self.do_layout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()

        for item in self.item_list:
            size = size.expandedTo(item.minimumSize())

        margin = self.contentsMargins().top() + self.contentsMargins().bottom()
        size += QSize(0, margin)

        return size

    def do_layout(self, rect, test_only):
        spacing = self.spacing()

        # Учитываем отступы
        contents_margins = self.contentsMargins()
        effective_rect = rect.adjusted(
            contents_margins.left(),
            contents_margins.top(),
            -contents_margins.right(),
            -contents_margins.bottom()
        )

        x = effective_rect.x()
        y = effective_rect.y()
        line_height = 0

        for item in self.item_list:
            widget = item.widget()
            if widget and not widget.isVisibleTo(self.parentWidget()):
                continue

            space_x = spacing
            space_y = spacing
            next_x = x + item.sizeHint().width() + space_x

            # Если не помещается в текущей строке, переходим на новую
            if next_x - effective_rect.x() > effective_rect.width() and line_height > 0:
                x = effective_rect.x()
                y = y + line_height + space_y
                next_x = x + item.sizeHint().width() + space_x
                line_height = 0

            if not test_only:
                item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))

            x = next_x
            line_height = max(line_height, item.sizeHint().height())

        return y + line_height - rect.y()