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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_search_list_item(object):
    def setupUi(self, search_list_item):
        if not search_list_item.objectName():
            search_list_item.setObjectName(u"search_list_item")
        search_list_item.resize(695, 60)
        search_list_item.setMinimumSize(QSize(695, 60))
        search_list_item.setBaseSize(QSize(695, 60))
        font = QFont()
        font.setUnderline(False)
        search_list_item.setFont(font)
        search_list_item.setFrameShape(QFrame.Shape.NoFrame)
        search_list_item.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(search_list_item)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.file_name = QLabel(search_list_item)
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
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setUnderline(False)
        self.file_name.setFont(font1)
        self.file_name.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.file_name)

        self.occurrence_counter = QLabel(search_list_item)
        self.occurrence_counter.setObjectName(u"occurrence_counter")
        sizePolicy.setHeightForWidth(self.occurrence_counter.sizePolicy().hasHeightForWidth())
        self.occurrence_counter.setSizePolicy(sizePolicy)
        self.occurrence_counter.setMinimumSize(QSize(0, 15))
        self.occurrence_counter.setMaximumSize(QSize(16777215, 15))
        self.occurrence_counter.setBaseSize(QSize(0, 15))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setUnderline(False)
        self.occurrence_counter.setFont(font2)
        self.occurrence_counter.setStyleSheet(u"color:rgb(120, 120, 120)")

        self.verticalLayout_2.addWidget(self.occurrence_counter)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.search_cards = QWidget(search_list_item)
        self.search_cards.setObjectName(u"search_cards")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.search_cards.sizePolicy().hasHeightForWidth())
        self.search_cards.setSizePolicy(sizePolicy1)
        self.search_cards.setMinimumSize(QSize(695, 0))
        self.search_cards.setBaseSize(QSize(695, 0))
        font3 = QFont()
        font3.setPointSize(32)
        font3.setUnderline(False)
        self.search_cards.setFont(font3)

        self.verticalLayout.addWidget(self.search_cards)


        self.retranslateUi(search_list_item)

        QMetaObject.connectSlotsByName(search_list_item)
    # setupUi

    def retranslateUi(self, search_list_item):
        search_list_item.setWindowTitle(QCoreApplication.translate("search_list_item", u"Frame", None))
        self.file_name.setText(QCoreApplication.translate("search_list_item", u"\u0424\u0430\u0439\u043b \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 pdf", None))
        self.occurrence_counter.setText(QCoreApplication.translate("search_list_item", u"\u041d\u0430\u0439\u0434\u0435\u043d\u043e \u0432\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0439 - ", None))
    # retranslateUi

