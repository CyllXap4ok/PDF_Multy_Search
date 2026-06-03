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
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSplitter, QVBoxLayout, QWidget)
import res_rc

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        if not GroupBox.objectName():
            GroupBox.setObjectName(u"GroupBox")
        GroupBox.resize(1366, 768)
        GroupBox.setMinimumSize(QSize(0, 0))
        GroupBox.setBaseSize(QSize(0, 0))
        GroupBox.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border:none;")
        GroupBox.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.verticalLayout_7 = QVBoxLayout(GroupBox)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(12, 10, 0, 10)
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
        self.clear_search_button.setEnabled(False)
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


        self.verticalLayout_7.addLayout(self.search_window_top_bar)

        self.splitter = QSplitter(GroupBox)
        self.splitter.setObjectName(u"splitter")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy3)
        self.splitter.setSizeIncrement(QSize(0, 0))
        self.splitter.setStyleSheet(u"QSplitter:handle {\n"
"    margin-left: 10px;\n"
"    margin-right: 10px;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    background-color: rgb(60, 60, 60)\n"
"}\n"
"\n"
"QSplitter::handle:pressed {\n"
"  background-color: rgb(80, 80, 80);\n"
"}")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setHandleWidth(2)
        self.splitter.setChildrenCollapsible(False)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.documents_table = QVBoxLayout(self.layoutWidget)
        self.documents_table.setSpacing(0)
        self.documents_table.setObjectName(u"documents_table")
        self.documents_table.setContentsMargins(0, 0, 0, 0)
        self.documents_table_headers = QFrame(self.layoutWidget)
        self.documents_table_headers.setObjectName(u"documents_table_headers")
        self.documents_table_headers.setMinimumSize(QSize(0, 30))
        self.documents_table_headers.setMaximumSize(QSize(16777215, 30))
        self.documents_table_headers.setBaseSize(QSize(0, 30))
        self.documents_table_headers.setStyleSheet(u"QFrame#file_table_headers {\n"
"	margin-right: 12px;\n"
"	border-bottom: 1px solid rgb(80, 80, 80);\n"
"}")
        self.files_table_headers = QHBoxLayout(self.documents_table_headers)
        self.files_table_headers.setSpacing(0)
        self.files_table_headers.setObjectName(u"files_table_headers")
        self.files_table_headers.setContentsMargins(0, 0, 0, 0)
        self.doc_name_header_container = QWidget(self.documents_table_headers)
        self.doc_name_header_container.setObjectName(u"doc_name_header_container")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.doc_name_header_container.sizePolicy().hasHeightForWidth())
        self.doc_name_header_container.setSizePolicy(sizePolicy4)
        self.doc_name_header_container.setStyleSheet(u"QWidget#file_name_header_container {\n"
"	border-right: 1px solid rgb(80, 80, 80);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.doc_name_header_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.doc_name_header = QLabel(self.doc_name_header_container)
        self.doc_name_header.setObjectName(u"doc_name_header")
        sizePolicy4.setHeightForWidth(self.doc_name_header.sizePolicy().hasHeightForWidth())
        self.doc_name_header.setSizePolicy(sizePolicy4)
        self.doc_name_header.setMinimumSize(QSize(0, 0))
        self.doc_name_header.setMaximumSize(QSize(16777215, 16777215))
        self.doc_name_header.setBaseSize(QSize(0, 0))
        self.doc_name_header.setStyleSheet(u"")
        self.doc_name_header.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.doc_name_header.setMargin(0)

        self.verticalLayout.addWidget(self.doc_name_header, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)


        self.files_table_headers.addWidget(self.doc_name_header_container)

        self.doc_type_header_container = QWidget(self.documents_table_headers)
        self.doc_type_header_container.setObjectName(u"doc_type_header_container")
        self.doc_type_header_container.setStyleSheet(u"QWidget#file_type_header_container {\n"
"	border-right: 1px solid rgb(80, 80, 80);\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.doc_type_header_container)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 0, 10, 0)
        self.file_type_header = QLabel(self.doc_type_header_container)
        self.file_type_header.setObjectName(u"file_type_header")

        self.verticalLayout_6.addWidget(self.file_type_header)


        self.files_table_headers.addWidget(self.doc_type_header_container)

        self.match_count_header_container = QWidget(self.documents_table_headers)
        self.match_count_header_container.setObjectName(u"match_count_header_container")
        self.match_count_header_container.setStyleSheet(u"QWidget#match_count_header_container {\n"
"	border-right: 1px solid rgb(80, 80, 80);\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.match_count_header_container)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.match_count_header = QLabel(self.match_count_header_container)
        self.match_count_header.setObjectName(u"match_count_header")
        sizePolicy.setHeightForWidth(self.match_count_header.sizePolicy().hasHeightForWidth())
        self.match_count_header.setSizePolicy(sizePolicy)
        self.match_count_header.setMinimumSize(QSize(0, 0))
        self.match_count_header.setMaximumSize(QSize(16777215, 16777215))
        self.match_count_header.setBaseSize(QSize(0, 0))
        self.match_count_header.setStyleSheet(u"")
        self.match_count_header.setLineWidth(0)
        self.match_count_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.match_count_header, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.files_table_headers.addWidget(self.match_count_header_container)

        self.search_status_header_container = QWidget(self.documents_table_headers)
        self.search_status_header_container.setObjectName(u"search_status_header_container")
        self.search_status_header_container.setMinimumSize(QSize(82, 0))
        self.search_status_header_container.setMaximumSize(QSize(82, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.search_status_header_container)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 0, 10, 0)
        self.search_status_header = QLabel(self.search_status_header_container)
        self.search_status_header.setObjectName(u"search_status_header")
        sizePolicy.setHeightForWidth(self.search_status_header.sizePolicy().hasHeightForWidth())
        self.search_status_header.setSizePolicy(sizePolicy)
        self.search_status_header.setMinimumSize(QSize(0, 0))
        self.search_status_header.setMaximumSize(QSize(16777215, 16777215))
        self.search_status_header.setBaseSize(QSize(0, 0))
        self.search_status_header.setStyleSheet(u"")
        self.search_status_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.search_status_header, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.files_table_headers.addWidget(self.search_status_header_container)


        self.documents_table.addWidget(self.documents_table_headers)

        self.documents_scroll_area = QScrollArea(self.layoutWidget)
        self.documents_scroll_area.setObjectName(u"documents_scroll_area")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.documents_scroll_area.sizePolicy().hasHeightForWidth())
        self.documents_scroll_area.setSizePolicy(sizePolicy5)
        self.documents_scroll_area.setMinimumSize(QSize(500, 0))
        self.documents_scroll_area.setBaseSize(QSize(0, 0))
        self.documents_scroll_area.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 12px;\n"
"    margin: 0px 3px 0px 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(60, 60, 60);\n"
"    min-height: 20px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(70, 70, 70)\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background: rgb(80, 80, 80);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-page:vertical, QScrollBar::add-page:vertical {\n"
"    background: transparent;\n"
"}")
        self.documents_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.documents_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.documents_scroll_area.setWidgetResizable(True)
        self.documents_list = QWidget()
        self.documents_list.setObjectName(u"documents_list")
        self.documents_list.setGeometry(QRect(0, 0, 544, 674))
        self.verticalLayout_2 = QVBoxLayout(self.documents_list)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.documents_scroll_area.setWidget(self.documents_list)

        self.documents_table.addWidget(self.documents_scroll_area)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.document_matches = QVBoxLayout(self.layoutWidget1)
        self.document_matches.setSpacing(0)
        self.document_matches.setObjectName(u"document_matches")
        self.document_matches.setContentsMargins(12, 0, 0, 0)
        self.document_name = QLabel(self.layoutWidget1)
        self.document_name.setObjectName(u"document_name")
        self.document_name.setMinimumSize(QSize(0, 30))
        self.document_name.setMaximumSize(QSize(16777215, 30))
        self.document_name.setBaseSize(QSize(0, 30))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.document_name.setFont(font2)
        self.document_name.setStyleSheet(u"border-bottom: 1px solid rgb(80, 80, 80);\n"
"margin-right: 12px;")
        self.document_name.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.document_matches.addWidget(self.document_name)

        self.search_results_scroll_area = QScrollArea(self.layoutWidget1)
        self.search_results_scroll_area.setObjectName(u"search_results_scroll_area")
        sizePolicy5.setHeightForWidth(self.search_results_scroll_area.sizePolicy().hasHeightForWidth())
        self.search_results_scroll_area.setSizePolicy(sizePolicy5)
        self.search_results_scroll_area.setMinimumSize(QSize(710, 0))
        self.search_results_scroll_area.setBaseSize(QSize(0, 0))
        self.search_results_scroll_area.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 12px;\n"
"    margin: 0px 3px 0px 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(60, 60, 60);\n"
"    min-height: 20px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(70, 70, 70)\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background: rgb(80, 80, 80);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-page:vertical, QScrollBar::add-page:vertical {\n"
"    background: transparent;\n"
"}")
        self.search_results_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.search_results_scroll_area.setWidgetResizable(True)
        self.search_list = QWidget()
        self.search_list.setObjectName(u"search_list")
        self.search_list.setGeometry(QRect(0, 0, 773, 674))
        self.search_results_scroll_area.setWidget(self.search_list)

        self.document_matches.addWidget(self.search_results_scroll_area)

        self.splitter.addWidget(self.layoutWidget1)

        self.verticalLayout_7.addWidget(self.splitter)

#if QT_CONFIG(shortcut)
        self.doc_name_header.setBuddy(self.documents_table_headers)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(GroupBox)

        QMetaObject.connectSlotsByName(GroupBox)
    # setupUi

    def retranslateUi(self, GroupBox):
        GroupBox.setWindowTitle(QCoreApplication.translate("GroupBox", u"GroupBox", None))
        self.return_button.setText(QCoreApplication.translate("GroupBox", u"\u2b60\u041d\u0430\u0437\u0430\u0434", None))
        self.search_field.setPlaceholderText(QCoreApplication.translate("GroupBox", u"\u041f\u043e\u0438\u0441\u043a...", None))
        self.clear_search_button.setText("")
        self.search_button.setText("")
        self.doc_name_header.setText(QCoreApplication.translate("GroupBox", u"\u0418\u043c\u044f \u0444\u0430\u0439\u043b\u0430", None))
        self.file_type_header.setText(QCoreApplication.translate("GroupBox", u"\u0422\u0438\u043f \u0444\u0430\u0439\u043b\u0430", None))
        self.match_count_header.setText(QCoreApplication.translate("GroupBox", u"\u0412\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0439", None))
        self.search_status_header.setText(QCoreApplication.translate("GroupBox", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.document_name.setText(QCoreApplication.translate("GroupBox", u"\u0418\u043c\u044f \u0444\u0430\u0439\u043b\u0430", None))
    # retranslateUi

