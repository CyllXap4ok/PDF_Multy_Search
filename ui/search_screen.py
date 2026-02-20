# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_screen.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGroupBox,
    QHBoxLayout, QListView, QPlainTextEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        if not GroupBox.objectName():
            GroupBox.setObjectName(u"GroupBox")
        GroupBox.resize(832, 492)
        GroupBox.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border:none;")
        GroupBox.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.verticalLayout = QVBoxLayout(GroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.search_window_top_bar = QHBoxLayout()
        self.search_window_top_bar.setSpacing(5)
        self.search_window_top_bar.setObjectName(u"search_window_top_bar")
        self.return_button = QPushButton(GroupBox)
        self.return_button.setObjectName(u"return_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.return_button.sizePolicy().hasHeightForWidth())
        self.return_button.setSizePolicy(sizePolicy)
        self.return_button.setMinimumSize(QSize(80, 30))
        self.return_button.setMaximumSize(QSize(80, 30))
        self.return_button.setBaseSize(QSize(80, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.return_button.setFont(font)
        self.return_button.setStyleSheet(u"QPushButton {\n"
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
        self.return_button.setIconSize(QSize(16, 16))

        self.search_window_top_bar.addWidget(self.return_button)

        self.frame = QFrame(GroupBox)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(700, 30))
        self.frame.setMaximumSize(QSize(16777215, 30))
        self.frame.setBaseSize(QSize(700, 0))
        self.frame.setStyleSheet(u"background-color:rgb(60, 60, 60);\n"
"border-radius:5px;")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Sunken)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit = QPlainTextEdit(self.frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy1.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy1)
        self.plainTextEdit.setMinimumSize(QSize(640, 30))
        self.plainTextEdit.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit.setBaseSize(QSize(640, 30))
        font1 = QFont()
        font1.setPointSize(10)
        self.plainTextEdit.setFont(font1)
        self.plainTextEdit.setStyleSheet(u"color:white;\n"
"padding-left:5px;\n"
"padding-top:2px;")
        self.plainTextEdit.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.plainTextEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.plainTextEdit.setFrameShadow(QFrame.Shadow.Sunken)
        self.plainTextEdit.setLineWidth(1)
        self.plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.plainTextEdit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.plainTextEdit.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

        self.horizontalLayout_2.addWidget(self.plainTextEdit)

        self.clear_search_button = QPushButton(self.frame)
        self.clear_search_button.setObjectName(u"clear_search_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.clear_search_button.sizePolicy().hasHeightForWidth())
        self.clear_search_button.setSizePolicy(sizePolicy2)
        self.clear_search_button.setMinimumSize(QSize(30, 30))
        self.clear_search_button.setMaximumSize(QSize(30, 30))
        self.clear_search_button.setBaseSize(QSize(30, 30))
        self.clear_search_button.setStyleSheet(u"QPushButton {\n"
"	border:0px;\n"
"	border-radius:3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:rgb(80, 80, 80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgb(60, 60, 60);\n"
"}")
        icon = QIcon(QIcon.fromTheme(u"edit-clear"))
        self.clear_search_button.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.clear_search_button)

        self.search_button = QPushButton(self.frame)
        self.search_button.setObjectName(u"search_button")
        sizePolicy2.setHeightForWidth(self.search_button.sizePolicy().hasHeightForWidth())
        self.search_button.setSizePolicy(sizePolicy2)
        self.search_button.setMinimumSize(QSize(30, 30))
        self.search_button.setMaximumSize(QSize(30, 30))
        self.search_button.setBaseSize(QSize(30, 30))
        self.search_button.setStyleSheet(u"QPushButton {\n"
"	border:0px;\n"
"	border-radius:3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:rgb(80, 80, 80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgb(60, 60, 60);\n"
"}")
        icon1 = QIcon(QIcon.fromTheme(u"edit-find"))
        self.search_button.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.search_button)


        self.search_window_top_bar.addWidget(self.frame)


        self.verticalLayout.addLayout(self.search_window_top_bar)

        self.found_list = QListView(GroupBox)
        self.found_list.setObjectName(u"found_list")
        self.found_list.setStyleSheet(u"background:transparent;\n"
"border:0px;")

        self.verticalLayout.addWidget(self.found_list)


        self.retranslateUi(GroupBox)

        QMetaObject.connectSlotsByName(GroupBox)
    # setupUi

    def retranslateUi(self, GroupBox):
        GroupBox.setWindowTitle(QCoreApplication.translate("GroupBox", u"GroupBox", None))
        self.return_button.setText(QCoreApplication.translate("GroupBox", u"\u2b60\u041d\u0430\u0437\u0430\u0434", None))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("GroupBox", u"\u041f\u043e\u0438\u0441\u043a...", None))
        self.clear_search_button.setText("")
        self.search_button.setText("")
    # retranslateUi

