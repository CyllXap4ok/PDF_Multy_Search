# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_file_item.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_search_file_item(object):
    def setupUi(self, search_file_item):
        if not search_file_item.objectName():
            search_file_item.setObjectName(u"search_file_item")
        search_file_item.resize(571, 30)
        search_file_item.setMinimumSize(QSize(0, 30))
        search_file_item.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout = QHBoxLayout(search_file_item)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 12, 0)
        self.file_name_container = QWidget(search_file_item)
        self.file_name_container.setObjectName(u"file_name_container")
        self.file_name_container.setStyleSheet(u"QWidget#file_name_container {\n"
"	border-right: 1px solid rgb(80, 80, 80);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.file_name_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.file_name = QLabel(self.file_name_container)
        self.file_name.setObjectName(u"file_name")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_name.sizePolicy().hasHeightForWidth())
        self.file_name.setSizePolicy(sizePolicy)
        self.file_name.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.file_name)


        self.horizontalLayout.addWidget(self.file_name_container)

        self.file_type_container = QWidget(search_file_item)
        self.file_type_container.setObjectName(u"file_type_container")
        self.file_type_container.setMinimumSize(QSize(82, 0))
        self.file_type_container.setMaximumSize(QSize(82, 16777215))
        self.file_type_container.setStyleSheet(u"QWidget#file_type_container {\n"
"	border-right: 1px solid rgb(80, 80, 80);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.file_type_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.file_type = QLabel(self.file_type_container)
        self.file_type.setObjectName(u"file_type")
        self.file_type.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.file_type)


        self.horizontalLayout.addWidget(self.file_type_container)

        self.match_count_container = QWidget(search_file_item)
        self.match_count_container.setObjectName(u"match_count_container")
        self.match_count_container.setMinimumSize(QSize(85, 0))
        self.match_count_container.setMaximumSize(QSize(85, 16777215))
        self.match_count_container.setStyleSheet(u"QWidget#match_count_container {\n"
"	border-right: 1px solid rgb(80, 80, 80);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.match_count_container)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.match_count = QLabel(self.match_count_container)
        self.match_count.setObjectName(u"match_count")
        self.match_count.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.match_count)


        self.horizontalLayout.addWidget(self.match_count_container)

        self.search_status_container = QWidget(search_file_item)
        self.search_status_container.setObjectName(u"search_status_container")
        self.search_status_container.setMinimumSize(QSize(82, 0))
        self.search_status_container.setMaximumSize(QSize(82, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.search_status_container)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.search_status = QLabel(self.search_status_container)
        self.search_status.setObjectName(u"search_status")
        self.search_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.search_status)


        self.horizontalLayout.addWidget(self.search_status_container)


        self.retranslateUi(search_file_item)

        QMetaObject.connectSlotsByName(search_file_item)
    # setupUi

    def retranslateUi(self, search_file_item):
        search_file_item.setWindowTitle(QCoreApplication.translate("search_file_item", u"Form", None))
        self.file_name.setText("")
        self.file_type.setText("")
        self.match_count.setText("")
        self.search_status.setText(QCoreApplication.translate("search_file_item", u"\u2014", None))
    # retranslateUi

