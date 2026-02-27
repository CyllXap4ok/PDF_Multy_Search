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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)
import res_rc

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        if not GroupBox.objectName():
            GroupBox.setObjectName(u"GroupBox")
        GroupBox.resize(719, 507)
        GroupBox.setMinimumSize(QSize(0, 0))
        GroupBox.setBaseSize(QSize(0, 0))
        GroupBox.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border:none;")
        GroupBox.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.verticalLayout = QVBoxLayout(GroupBox)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 10, 0, 10)
        self.search_window_top_bar = QHBoxLayout()
        self.search_window_top_bar.setSpacing(5)
        self.search_window_top_bar.setObjectName(u"search_window_top_bar")
        self.search_window_top_bar.setContentsMargins(-1, -1, 12, -1)
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
        self.frame.setMinimumSize(QSize(0, 30))
        self.frame.setMaximumSize(QSize(16777215, 30))
        self.frame.setBaseSize(QSize(0, 0))
        self.frame.setStyleSheet(u"background-color:rgb(60, 60, 60);\n"
"border-radius:5px;")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Sunken)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.search_field = QLineEdit(self.frame)
        self.search_field.setObjectName(u"search_field")
        sizePolicy1.setHeightForWidth(self.search_field.sizePolicy().hasHeightForWidth())
        self.search_field.setSizePolicy(sizePolicy1)
        self.search_field.setMinimumSize(QSize(0, 30))
        self.search_field.setMaximumSize(QSize(16777215, 30))
        self.search_field.setBaseSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(10)
        self.search_field.setFont(font1)
        self.search_field.setStyleSheet(u"color: white;\n"
"padding-left: 5px;\n"
"padding-top: -2px;")
        self.search_field.setMaxLength(1000)
        self.search_field.setFrame(False)
        self.search_field.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.search_field)

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

        self.scrollArea = QScrollArea(GroupBox)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(707, 450))
        self.scrollArea.setBaseSize(QSize(707, 450))
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 12px;\n"
"    margin: 0px 3px 0px 4px;\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u0437\u0443\u043d\u043e\u043a \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(60, 60, 60);\n"
"    min-height: 20px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u0437\u0443\u043d\u043e\u043a \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(70, 70, 70)\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u0437\u0443\u043d\u043e\u043a \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background: rgb(80, 80, 80);\n"
"}\n"
"\n"
"/* \u0421\u0442\u0440\u0435\u043b\u043a\u0438 \u0432\u0432\u0435\u0440\u0445/\u0432\u043d\u0438\u0437 */\n"
"QScr"
                        "ollBar::sub-line:vertical, QScrollBar::add-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"/* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0444\u043e\u043d \u043c\u0435\u0436\u0434\u0443 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u043e\u043c \u0438 \u0441\u0442\u0440\u0435\u043b\u043a\u0430\u043c\u0438 */\n"
"QScrollBar::sub-page:vertical, QScrollBar::add-page:vertical {\n"
"    background: transparent;\n"
"}")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.search_list = QWidget()
        self.search_list.setObjectName(u"search_list")
        self.search_list.setGeometry(QRect(0, 0, 707, 450))
        self.scrollArea.setWidget(self.search_list)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(GroupBox)

        QMetaObject.connectSlotsByName(GroupBox)
    # setupUi

    def retranslateUi(self, GroupBox):
        GroupBox.setWindowTitle(QCoreApplication.translate("GroupBox", u"GroupBox", None))
        self.return_button.setText(QCoreApplication.translate("GroupBox", u"\u2b60\u041d\u0430\u0437\u0430\u0434", None))
        self.search_field.setPlaceholderText(QCoreApplication.translate("GroupBox", u"\u041f\u043e\u0438\u0441\u043a...", None))
        self.clear_search_button.setText("")
        self.search_button.setText("")
    # retranslateUi

