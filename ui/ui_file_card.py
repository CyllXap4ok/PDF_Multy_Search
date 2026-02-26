# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_card.ui'
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

class Ui_file_card(object):
    def setupUi(self, file_card):
        if not file_card.objectName():
            file_card.setObjectName(u"file_card")
        file_card.resize(170, 170)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(file_card.sizePolicy().hasHeightForWidth())
        file_card.setSizePolicy(sizePolicy)
        file_card.setMinimumSize(QSize(170, 170))
        file_card.setMaximumSize(QSize(170, 170))
        file_card.setBaseSize(QSize(170, 170))
        file_card.setStyleSheet(u"QFrame {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(50, 50, 50, 255), stop:1 rgba(70, 70, 70, 255));\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	background-color: rgba(155, 255, 252, 30);\n"
"}")
        self.verticalLayout = QVBoxLayout(file_card)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.file_icon = QLabel(file_card)
        self.file_icon.setObjectName(u"file_icon")
        sizePolicy.setHeightForWidth(self.file_icon.sizePolicy().hasHeightForWidth())
        self.file_icon.setSizePolicy(sizePolicy)
        self.file_icon.setMinimumSize(QSize(100, 100))
        self.file_icon.setMaximumSize(QSize(100, 100))
        self.file_icon.setBaseSize(QSize(100, 100))
        font = QFont()
        font.setPointSize(72)
        font.setKerning(True)
        self.file_icon.setFont(font)
        self.file_icon.setStyleSheet(u"background:transparent;\n"
"margin-top:-18px;")
        self.file_icon.setScaledContents(False)
        self.file_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.file_icon, 0, Qt.AlignmentFlag.AlignHCenter)

        self.file_name = QLabel(file_card)
        self.file_name.setObjectName(u"file_name")
        sizePolicy.setHeightForWidth(self.file_name.sizePolicy().hasHeightForWidth())
        self.file_name.setSizePolicy(sizePolicy)
        self.file_name.setMinimumSize(QSize(160, 30))
        self.file_name.setMaximumSize(QSize(160, 30))
        self.file_name.setBaseSize(QSize(160, 30))
        font1 = QFont()
        font1.setPointSize(8)
        self.file_name.setFont(font1)
        self.file_name.setStyleSheet(u"background:transparent;")
        self.file_name.setFrameShadow(QFrame.Shadow.Plain)
        self.file_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.file_name.setWordWrap(True)
        self.file_name.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout.addWidget(self.file_name, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(file_card)

        QMetaObject.connectSlotsByName(file_card)
    # setupUi

    def retranslateUi(self, file_card):
        file_card.setWindowTitle(QCoreApplication.translate("file_card", u"Frame", None))
        self.file_icon.setText(QCoreApplication.translate("file_card", u"\U0001f4d1", None))
        self.file_name.setText(QCoreApplication.translate("file_card", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442...pdf", None))
    # retranslateUi

