# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_list_item.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_search_list_item(object):
    def setupUi(self, search_list_item):
        if not search_list_item.objectName():
            search_list_item.setObjectName(u"search_list_item")
        search_list_item.resize(695, 45)
        search_list_item.setMinimumSize(QSize(695, 45))
        search_list_item.setBaseSize(QSize(695, 45))
        font = QFont()
        font.setUnderline(False)
        search_list_item.setFont(font)
        search_list_item.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout = QVBoxLayout(search_list_item)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.search_item_header = QWidget(search_list_item)
        self.search_item_header.setObjectName(u"search_item_header")
        self.search_item_header.setMinimumSize(QSize(0, 25))
        self.search_item_header.setMaximumSize(QSize(16777215, 25))
        self.search_item_header.setBaseSize(QSize(0, 25))
        self.search_item_header.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.search_item_header.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.search_item_header.setStyleSheet(u"QWidget:hover {\n"
"	background-color: rgb(50, 50, 50);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.search_item_header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.file_name = QLabel(self.search_item_header)
        self.file_name.setObjectName(u"file_name")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_name.sizePolicy().hasHeightForWidth())
        self.file_name.setSizePolicy(sizePolicy)
        self.file_name.setMinimumSize(QSize(0, 25))
        self.file_name.setMaximumSize(QSize(16777215, 25))
        self.file_name.setBaseSize(QSize(0, 25))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setUnderline(False)
        self.file_name.setFont(font1)

        self.horizontalLayout.addWidget(self.file_name)

        self.hide_results_button = QPushButton(self.search_item_header)
        self.hide_results_button.setObjectName(u"hide_results_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.hide_results_button.sizePolicy().hasHeightForWidth())
        self.hide_results_button.setSizePolicy(sizePolicy1)
        self.hide_results_button.setMinimumSize(QSize(25, 25))
        self.hide_results_button.setMaximumSize(QSize(25, 25))
        self.hide_results_button.setBaseSize(QSize(25, 25))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setUnderline(False)
        self.hide_results_button.setFont(font2)
        self.hide_results_button.setStyleSheet(u"background:transparent;\n"
"border:none")

        self.horizontalLayout.addWidget(self.hide_results_button)


        self.verticalLayout.addWidget(self.search_item_header)

        self.occurrence_counter = QLabel(search_list_item)
        self.occurrence_counter.setObjectName(u"occurrence_counter")
        sizePolicy.setHeightForWidth(self.occurrence_counter.sizePolicy().hasHeightForWidth())
        self.occurrence_counter.setSizePolicy(sizePolicy)
        self.occurrence_counter.setMinimumSize(QSize(0, 15))
        self.occurrence_counter.setMaximumSize(QSize(16777215, 15))
        self.occurrence_counter.setBaseSize(QSize(0, 15))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setUnderline(False)
        self.occurrence_counter.setFont(font3)
        self.occurrence_counter.setStyleSheet(u"color:rgb(120, 120, 120)")

        self.verticalLayout.addWidget(self.occurrence_counter)


        self.retranslateUi(search_list_item)

        QMetaObject.connectSlotsByName(search_list_item)
    # setupUi

    def retranslateUi(self, search_list_item):
        search_list_item.setWindowTitle(QCoreApplication.translate("search_list_item", u"Frame", None))
        self.file_name.setText(QCoreApplication.translate("search_list_item", u"\u0424\u0430\u0439\u043b \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 pdf", None))
        self.hide_results_button.setText(QCoreApplication.translate("search_list_item", u"\u25bc", None))
        self.occurrence_counter.setText(QCoreApplication.translate("search_list_item", u"\u041d\u0430\u0439\u0434\u0435\u043d\u043e \u0432\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0439 - ", None))
    # retranslateUi

