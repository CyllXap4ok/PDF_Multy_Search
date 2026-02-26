# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_card.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_search_card(object):
    def setupUi(self, search_card):
        if not search_card.objectName():
            search_card.setObjectName(u"search_card")
        search_card.resize(225, 50)
        search_card.setMinimumSize(QSize(225, 50))
        search_card.setMaximumSize(QSize(225, 16777215))
        search_card.setBaseSize(QSize(225, 50))
        search_card.setStyleSheet(u"QFrame {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(50, 50, 50, 255), stop:1 rgba(70, 70, 70, 255));\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	background-color: rgba(155, 255, 252, 30);\n"
"}")
        self.verticalLayout = QVBoxLayout(search_card)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.occurrence_page_number = QLabel(search_card)
        self.occurrence_page_number.setObjectName(u"occurrence_page_number")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.occurrence_page_number.sizePolicy().hasHeightForWidth())
        self.occurrence_page_number.setSizePolicy(sizePolicy)
        self.occurrence_page_number.setMinimumSize(QSize(16, 0))
        self.occurrence_page_number.setMaximumSize(QSize(16777215, 16))
        self.occurrence_page_number.setBaseSize(QSize(0, 16))
        font = QFont()
        font.setBold(True)
        self.occurrence_page_number.setFont(font)
        self.occurrence_page_number.setStyleSheet(u"background:transparent;")

        self.verticalLayout.addWidget(self.occurrence_page_number, 0, Qt.AlignmentFlag.AlignTop)

        self.occurrence_text = QLabel(search_card)
        self.occurrence_text.setObjectName(u"occurrence_text")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.occurrence_text.sizePolicy().hasHeightForWidth())
        self.occurrence_text.setSizePolicy(sizePolicy1)
        self.occurrence_text.setStyleSheet(u"background:transparent;\n"
"margin-left:2px;")
        self.occurrence_text.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.occurrence_text.setWordWrap(True)
        self.occurrence_text.setMargin(0)
        self.occurrence_text.setIndent(-1)

        self.verticalLayout.addWidget(self.occurrence_text)


        self.retranslateUi(search_card)

        QMetaObject.connectSlotsByName(search_card)
    # setupUi

    def retranslateUi(self, search_card):
        search_card.setWindowTitle(QCoreApplication.translate("search_card", u"Frame", None))
        self.occurrence_page_number.setText(QCoreApplication.translate("search_card", u"\U0001f4c4 \U00000421\U00000442\U00000440\U00000430\U0000043d\U00000438\U00000446\U00000430 \U00002116", None))
        self.occurrence_text.setText(QCoreApplication.translate("search_card", u"\u0422\u0435\u043a\u0441\u0442 \u0432\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
    # retranslateUi

