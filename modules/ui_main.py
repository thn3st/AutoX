# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainEtYbtQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1150, 647)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        self.tab_autox = QWidget()
        self.tab_autox.setObjectName(u"tab_autox")
        self.verticalLayout_2 = QVBoxLayout(self.tab_autox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 5)
        self.btn_start_all = QPushButton(self.tab_autox)
        self.btn_start_all.setObjectName(u"btn_start_all")
        self.btn_start_all.setEnabled(True)
        self.btn_start_all.setMinimumSize(QSize(0, 40))
        self.btn_start_all.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start_all.setStyleSheet(u"QPushButton {\n"
"	color: #fff;\n"
"	background-color: rgb(25, 135, 84);\n"
"	border: 1px solid rgb(25, 135, 84);\n"
"	border-radius: 2px;\n"
"	cursor: pointer;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(21, 113, 70);\n"
"	border: 1px solid rgb(21, 113, 70);\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	padding-left: 2px;\n"
"	padding-top: 2px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(12, 101, 227);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.btn_start_all)

        self.btn_stop_all = QPushButton(self.tab_autox)
        self.btn_stop_all.setObjectName(u"btn_stop_all")
        self.btn_stop_all.setEnabled(True)
        self.btn_stop_all.setMinimumSize(QSize(0, 40))
        self.btn_stop_all.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_stop_all.setStyleSheet(u"QPushButton {\n"
"	color: #fff;\n"
"	background-color: #dc3545;\n"
"	border: 1px solid #dc3545;\n"
"	border-radius: 2px;\n"
"	cursor: pointer;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #bb2d3b;\n"
"	border: 1px solid #bb2d3b;\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	padding-left: 2px;\n"
"	padding-top: 2px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	\n"
"	background-color: rgb(197, 47, 62);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.btn_stop_all)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 5)
        self.btn_import_devices = QPushButton(self.tab_autox)
        self.btn_import_devices.setObjectName(u"btn_import_devices")
        self.btn_import_devices.setEnabled(True)
        self.btn_import_devices.setMinimumSize(QSize(0, 40))
        self.btn_import_devices.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_import_devices.setStyleSheet(u"QPushButton {\n"
"	color: #fff;\n"
"	background-color: #0d6efd;\n"
"	border: 1px solid #0d6efd;\n"
"	border-radius: 2px;\n"
"	cursor: pointer;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #0b5ed7;\n"
"	border: 1px solid #0b5ed7;\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	padding-left: 2px;\n"
"	padding-top: 2px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(12, 101, 227);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_import_devices)

        self.btn_import_accounts = QPushButton(self.tab_autox)
        self.btn_import_accounts.setObjectName(u"btn_import_accounts")
        self.btn_import_accounts.setEnabled(True)
        self.btn_import_accounts.setMinimumSize(QSize(0, 40))
        self.btn_import_accounts.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_import_accounts.setStyleSheet(u"QPushButton {\n"
"	color: #fff;\n"
"	background-color: #0d6efd;\n"
"	border: 1px solid #0d6efd;\n"
"	border-radius: 2px;\n"
"	cursor: pointer;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #0b5ed7;\n"
"	border: 1px solid #0b5ed7;\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	padding-left: 2px;\n"
"	padding-top: 2px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(12, 101, 227);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_import_accounts)

        self.btn_open_setting = QPushButton(self.tab_autox)
        self.btn_open_setting.setObjectName(u"btn_open_setting")
        self.btn_open_setting.setEnabled(True)
        self.btn_open_setting.setMinimumSize(QSize(0, 40))
        self.btn_open_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open_setting.setStyleSheet(u"QPushButton {\n"
"	color: #fff;\n"
"	background-color: #0d6efd;\n"
"	border: 1px solid #0d6efd;\n"
"	border-radius: 2px;\n"
"	cursor: pointer;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #0b5ed7;\n"
"	border: 1px solid #0b5ed7;\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	padding-left: 2px;\n"
"	padding-top: 2px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(12, 101, 227);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_open_setting)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tb_accounts = QTableWidget(self.tab_autox)
        if (self.tb_accounts.columnCount() < 9):
            self.tb_accounts.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_accounts.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_accounts.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_accounts.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_accounts.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_accounts.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_accounts.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_accounts.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_accounts.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_accounts.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tb_accounts.setObjectName(u"tb_accounts")
        self.tb_accounts.setStyleSheet(u"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	color: #fff;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    height: 12px;\n"
"}")
        self.tb_accounts.setFrameShape(QFrame.NoFrame)
        self.tb_accounts.setFrameShadow(QFrame.Sunken)
        self.tb_accounts.setLineWidth(1)
        self.tb_accounts.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tb_accounts.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_accounts.setShowGrid(True)
        self.tb_accounts.setGridStyle(Qt.SolidLine)
        self.tb_accounts.setSortingEnabled(True)
        self.tb_accounts.setWordWrap(True)
        self.tb_accounts.setCornerButtonEnabled(True)
        self.tb_accounts.setRowCount(0)
        self.tb_accounts.horizontalHeader().setCascadingSectionResizes(True)
        self.tb_accounts.horizontalHeader().setMinimumSectionSize(54)
        self.tb_accounts.horizontalHeader().setDefaultSectionSize(200)
        self.tb_accounts.horizontalHeader().setProperty("showSortIndicator", True)
        self.tb_accounts.horizontalHeader().setStretchLastSection(True)
        self.tb_accounts.verticalHeader().setVisible(False)
        self.tb_accounts.verticalHeader().setCascadingSectionResizes(False)
        self.tb_accounts.verticalHeader().setProperty("showSortIndicator", False)
        self.tb_accounts.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tb_accounts)

        self.tabs.addTab(self.tab_autox, "")
        self.tab_logs = QWidget()
        self.tab_logs.setObjectName(u"tab_logs")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_logs)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.txt_logs = QPlainTextEdit(self.tab_logs)
        self.txt_logs.setObjectName(u"txt_logs")
        self.txt_logs.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.txt_logs)

        self.tabs.addTab(self.tab_logs, "")

        self.verticalLayout_3.addWidget(self.tabs)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 10, -1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.txt_total_count = QLabel(self.centralwidget)
        self.txt_total_count.setObjectName(u"txt_total_count")

        self.horizontalLayout_4.addWidget(self.txt_total_count)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.txt_selected_count = QLabel(self.centralwidget)
        self.txt_selected_count.setObjectName(u"txt_selected_count")

        self.horizontalLayout_4.addWidget(self.txt_selected_count)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.txt_running_count = QLabel(self.centralwidget)
        self.txt_running_count.setObjectName(u"txt_running_count")
        sizePolicy.setHeightForWidth(self.txt_running_count.sizePolicy().hasHeightForWidth())
        self.txt_running_count.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.txt_running_count)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.txt_total_running_count = QLabel(self.centralwidget)
        self.txt_total_running_count.setObjectName(u"txt_total_running_count")
        sizePolicy.setHeightForWidth(self.txt_total_running_count.sizePolicy().hasHeightForWidth())
        self.txt_total_running_count.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.txt_total_running_count)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.txt_version = QLabel(self.centralwidget)
        self.txt_version.setObjectName(u"txt_version")
        sizePolicy.setHeightForWidth(self.txt_version.sizePolicy().hasHeightForWidth())
        self.txt_version.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txt_version.setFont(font)

        self.horizontalLayout_4.addWidget(self.txt_version)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_start_all.setText(QCoreApplication.translate("MainWindow", u"CH\u1ea0Y", None))
        self.btn_stop_all.setText(QCoreApplication.translate("MainWindow", u"D\u1eeaNG", None))
        self.btn_import_devices.setText(QCoreApplication.translate("MainWindow", u"TH\u00caM DEVICES", None))
        self.btn_import_accounts.setText(QCoreApplication.translate("MainWindow", u"TH\u00caM T\u00c0I KHO\u1ea2N", None))
        self.btn_open_setting.setText(QCoreApplication.translate("MainWindow", u"M\u1ede C\u00c0I \u0110\u1eb6T", None))
        ___qtablewidgetitem = self.tb_accounts.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"stt", None));
        ___qtablewidgetitem1 = self.tb_accounts.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"device", None));
        ___qtablewidgetitem2 = self.tb_accounts.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"user", None));
        ___qtablewidgetitem3 = self.tb_accounts.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"pass", None));
        ___qtablewidgetitem4 = self.tb_accounts.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"2fa", None));
        ___qtablewidgetitem5 = self.tb_accounts.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"mail", None));
        ___qtablewidgetitem6 = self.tb_accounts.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"pass mail", None));
        ___qtablewidgetitem7 = self.tb_accounts.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"proxy", None));
        ___qtablewidgetitem8 = self.tb_accounts.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ti\u1ebfn tr\u00ecnh", None));
        self.tabs.setTabText(self.tabs.indexOf(self.tab_autox), QCoreApplication.translate("MainWindow", u"AutoX", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_logs), QCoreApplication.translate("MainWindow", u"Logs", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"T\u1ed5ng:", None))
        self.txt_total_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0110\u00e3 ch\u1ecdn:", None))
        self.txt_selected_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0110ang ch\u1ea1y:", None))
        self.txt_running_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.txt_total_running_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"VERSION:", None))
        self.txt_version.setText(QCoreApplication.translate("MainWindow", u"1.0.0", None))
    # retranslateUi

