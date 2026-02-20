# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_selection_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_file_selection_screen(object):
    def setupUi(self, file_selection_screen):
        if not file_selection_screen.objectName():
            file_selection_screen.setObjectName(u"file_selection_screen")
        file_selection_screen.resize(653, 538)
        file_selection_screen.setStyleSheet(u"border:none;")
        self.verticalLayout = QVBoxLayout(file_selection_screen)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.file_screen_top_bar = QHBoxLayout()
        self.file_screen_top_bar.setSpacing(2)
        self.file_screen_top_bar.setObjectName(u"file_screen_top_bar")
        self.label = QLabel(file_selection_screen)
        self.label.setObjectName(u"label")

        self.file_screen_top_bar.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.file_screen_top_bar.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.select_all_button = QCheckBox(file_selection_screen)
        self.select_all_button.setObjectName(u"select_all_button")
        font = QFont()
        font.setKerning(True)
        self.select_all_button.setFont(font)
        self.select_all_button.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.select_all_button)

        self.selection_cancel_button = QPushButton(file_selection_screen)
        self.selection_cancel_button.setObjectName(u"selection_cancel_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selection_cancel_button.sizePolicy().hasHeightForWidth())
        self.selection_cancel_button.setSizePolicy(sizePolicy)
        self.selection_cancel_button.setMinimumSize(QSize(90, 30))
        self.selection_cancel_button.setMaximumSize(QSize(90, 30))
        self.selection_cancel_button.setBaseSize(QSize(90, 30))
        font1 = QFont()
        font1.setBold(True)
        self.selection_cancel_button.setFont(font1)
        self.selection_cancel_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border-radius: 5px;\n"
"	padding-top: -2px;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 70, 70);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(50, 50, 50);\n"
"	margin: 1px;\n"
"	font-size: 12px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/deselect_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.selection_cancel_button.setIcon(icon)

        self.horizontalLayout.addWidget(self.selection_cancel_button)


        self.file_screen_top_bar.addLayout(self.horizontalLayout)

        self.delete_button = QPushButton(file_selection_screen)
        self.delete_button.setObjectName(u"delete_button")
        sizePolicy.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy)
        self.delete_button.setMinimumSize(QSize(90, 30))
        self.delete_button.setMaximumSize(QSize(90, 30))
        self.delete_button.setBaseSize(QSize(90, 30))
        self.delete_button.setFont(font1)
        self.delete_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border-radius: 5px;\n"
"	padding-top: -2px;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 70, 70);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(50, 50, 50);\n"
"	margin: 1px;\n"
"	font-size: 12px;\n"
"}")
        icon1 = QIcon(QIcon.fromTheme(u"edit-delete"))
        self.delete_button.setIcon(icon1)

        self.file_screen_top_bar.addWidget(self.delete_button)


        self.verticalLayout.addLayout(self.file_screen_top_bar)

        self.scrollArea = QScrollArea(file_selection_screen)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShadow(QFrame.Shadow.Sunken)
        self.scrollArea.setWidgetResizable(True)
        self.files_grid = QWidget()
        self.files_grid.setObjectName(u"files_grid")
        self.files_grid.setGeometry(QRect(0, 0, 635, 442))
        self.files_grid_layout = QGridLayout(self.files_grid)
        self.files_grid_layout.setSpacing(2)
        self.files_grid_layout.setObjectName(u"files_grid_layout")
        self.files_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.files_grid)

        self.verticalLayout.addWidget(self.scrollArea)

        self.file_screen_bottom_bar = QHBoxLayout()
        self.file_screen_bottom_bar.setObjectName(u"file_screen_bottom_bar")
        self.add_button = QPushButton(file_selection_screen)
        self.add_button.setObjectName(u"add_button")
        sizePolicy.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy)
        self.add_button.setMinimumSize(QSize(140, 30))
        self.add_button.setMaximumSize(QSize(140, 30))
        self.add_button.setBaseSize(QSize(140, 30))
        self.add_button.setFont(font1)
        self.add_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border-radius: 5px;\n"
"	padding-top: -2px;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 70, 70);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(50, 50, 50);\n"
"	margin: 1px;\n"
"	font-size: 12px;\n"
"}")

        self.file_screen_bottom_bar.addWidget(self.add_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.file_screen_bottom_bar.addItem(self.horizontalSpacer_2)

        self.button_next = QPushButton(file_selection_screen)
        self.button_next.setObjectName(u"button_next")
        sizePolicy.setHeightForWidth(self.button_next.sizePolicy().hasHeightForWidth())
        self.button_next.setSizePolicy(sizePolicy)
        self.button_next.setMinimumSize(QSize(80, 30))
        self.button_next.setMaximumSize(QSize(80, 30))
        self.button_next.setBaseSize(QSize(80, 30))
        self.button_next.setFont(font1)
        self.button_next.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border-radius: 5px;\n"
"	padding-top: -2px;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 70, 70);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(50, 50, 50);\n"
"	margin: 1px;\n"
"	font-size: 12px;\n"
"}")

        self.file_screen_bottom_bar.addWidget(self.button_next)


        self.verticalLayout.addLayout(self.file_screen_bottom_bar)


        self.retranslateUi(file_selection_screen)

        QMetaObject.connectSlotsByName(file_selection_screen)
    # setupUi

    def retranslateUi(self, file_selection_screen):
        file_selection_screen.setWindowTitle(QCoreApplication.translate("file_selection_screen", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("file_selection_screen", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b\u044b...", None))
        self.select_all_button.setText(QCoreApplication.translate("file_selection_screen", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0432\u0441\u0435", None))
        self.selection_cancel_button.setText(QCoreApplication.translate("file_selection_screen", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.delete_button.setText(QCoreApplication.translate("file_selection_screen", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.add_button.setText(QCoreApplication.translate("file_selection_screen", u"\U0001f4d1\U00000412\U0000044b\U00000431\U00000440\U00000430\U00000442\U0000044c \U00000444\U00000430\U00000439\U0000043b\U0000044b", None))
        self.button_next.setText(QCoreApplication.translate("file_selection_screen", u"\u0414\u0430\u043b\u0435\u0435\u2b62", None))
    # retranslateUi

