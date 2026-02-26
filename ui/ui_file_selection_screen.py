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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import res_rc

class Ui_file_selection_screen(object):
    def setupUi(self, file_selection_screen):
        if not file_selection_screen.objectName():
            file_selection_screen.setObjectName(u"file_selection_screen")
        file_selection_screen.resize(727, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(file_selection_screen.sizePolicy().hasHeightForWidth())
        file_selection_screen.setSizePolicy(sizePolicy)
        file_selection_screen.setMinimumSize(QSize(727, 550))
        file_selection_screen.setBaseSize(QSize(727, 550))
        file_selection_screen.setStyleSheet(u"border:none;")
        self.verticalLayout = QVBoxLayout(file_selection_screen)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 10, 0, 10)
        self.file_screen_top_bar = QHBoxLayout()
        self.file_screen_top_bar.setSpacing(2)
        self.file_screen_top_bar.setObjectName(u"file_screen_top_bar")
        self.file_screen_top_bar.setContentsMargins(-1, -1, 16, -1)
        self.label = QLabel(file_selection_screen)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setBaseSize(QSize(0, 30))

        self.file_screen_top_bar.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.file_screen_top_bar.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.select_all_button = QCheckBox(file_selection_screen)
        self.select_all_button.setObjectName(u"select_all_button")
        sizePolicy1.setHeightForWidth(self.select_all_button.sizePolicy().hasHeightForWidth())
        self.select_all_button.setSizePolicy(sizePolicy1)
        self.select_all_button.setMinimumSize(QSize(0, 30))
        self.select_all_button.setMaximumSize(QSize(16777215, 30))
        self.select_all_button.setBaseSize(QSize(0, 30))
        font = QFont()
        font.setKerning(True)
        self.select_all_button.setFont(font)
        self.select_all_button.setStyleSheet(u"QCheckBox {\n"
"    spacing: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #bfc5cc;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 2px solid #4a90e2;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #4a90e2;\n"
"    border: 2px solid #4a90e2;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    background-color: #357ABD;\n"
"    border: 2px solid #357ABD;\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"    background-color: #e0e0e0;\n"
"    border: 2px solid #c0c0c0;\n"
"}")
        self.select_all_button.setChecked(False)

        self.horizontalLayout.addWidget(self.select_all_button)

        self.selection_cancel_button = QPushButton(file_selection_screen)
        self.selection_cancel_button.setObjectName(u"selection_cancel_button")
        sizePolicy1.setHeightForWidth(self.selection_cancel_button.sizePolicy().hasHeightForWidth())
        self.selection_cancel_button.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy1)
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
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: gray;\n"
"}")
        icon1 = QIcon(QIcon.fromTheme(u"edit-delete"))
        self.delete_button.setIcon(icon1)

        self.file_screen_top_bar.addWidget(self.delete_button)


        self.verticalLayout.addLayout(self.file_screen_top_bar)

        self.scrollArea = QScrollArea(file_selection_screen)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy2)
        self.scrollArea.setFrameShadow(QFrame.Shadow.Sunken)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.files_grid = QWidget()
        self.files_grid.setObjectName(u"files_grid")
        self.files_grid.setGeometry(QRect(0, 0, 712, 454))
        sizePolicy.setHeightForWidth(self.files_grid.sizePolicy().hasHeightForWidth())
        self.files_grid.setSizePolicy(sizePolicy)
        self.files_grid.setMinimumSize(QSize(0, 0))
        self.files_grid.setBaseSize(QSize(0, 0))
        self.scrollArea.setWidget(self.files_grid)

        self.verticalLayout.addWidget(self.scrollArea)

        self.file_screen_bottom_bar = QHBoxLayout()
        self.file_screen_bottom_bar.setObjectName(u"file_screen_bottom_bar")
        self.file_screen_bottom_bar.setContentsMargins(-1, -1, 16, -1)
        self.add_button = QPushButton(file_selection_screen)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy1)
        self.add_button.setMinimumSize(QSize(120, 30))
        self.add_button.setMaximumSize(QSize(120, 30))
        self.add_button.setBaseSize(QSize(120, 30))
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
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: gray;\n"
"}")

        self.file_screen_bottom_bar.addWidget(self.add_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.file_screen_bottom_bar.addItem(self.horizontalSpacer_2)

        self.button_next = QPushButton(file_selection_screen)
        self.button_next.setObjectName(u"button_next")
        self.button_next.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button_next.sizePolicy().hasHeightForWidth())
        self.button_next.setSizePolicy(sizePolicy1)
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
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: gray;\n"
"}")
        self.button_next.setFlat(False)

        self.file_screen_bottom_bar.addWidget(self.button_next)


        self.verticalLayout.addLayout(self.file_screen_bottom_bar)


        self.retranslateUi(file_selection_screen)

        QMetaObject.connectSlotsByName(file_selection_screen)
    # setupUi

    def retranslateUi(self, file_selection_screen):
        file_selection_screen.setWindowTitle(QCoreApplication.translate("file_selection_screen", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("file_selection_screen", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u043e \u0444\u0430\u0439\u043b\u043e\u0432 - 0", None))
        self.select_all_button.setText(QCoreApplication.translate("file_selection_screen", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0432\u0441\u0435", None))
        self.selection_cancel_button.setText(QCoreApplication.translate("file_selection_screen", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.delete_button.setText(QCoreApplication.translate("file_selection_screen", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.add_button.setText(QCoreApplication.translate("file_selection_screen", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.button_next.setText(QCoreApplication.translate("file_selection_screen", u"\u0414\u0430\u043b\u0435\u0435\u2b62", None))
    # retranslateUi

