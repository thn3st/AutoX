# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'import_accountpMNdnJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_ImportAccountDialog(object):
    def setupUi(self, ImportAccountDialog):
        if not ImportAccountDialog.objectName():
            ImportAccountDialog.setObjectName(u"ImportAccountDialog")
        ImportAccountDialog.resize(1161, 706)
        self.verticalLayout = QVBoxLayout(ImportAccountDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_category = QLineEdit(ImportAccountDialog)
        self.txt_category.setObjectName(u"txt_category")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_category.sizePolicy().hasHeightForWidth())
        self.txt_category.setSizePolicy(sizePolicy)
        self.txt_category.setMinimumSize(QSize(120, 0))
        self.txt_category.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_2.addWidget(self.txt_category)

        self.btn_add = QPushButton(ImportAccountDialog)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy1)
        self.btn_add.setMinimumSize(QSize(0, 0))
        self.btn_add.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.btn_add)

        self.btn_edit = QPushButton(ImportAccountDialog)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.btn_edit.sizePolicy().hasHeightForWidth())
        self.btn_edit.setSizePolicy(sizePolicy1)
        self.btn_edit.setMinimumSize(QSize(0, 0))
        self.btn_edit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_edit.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.btn_edit)

        self.label = QLabel(ImportAccountDialog)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.label)

        self.cbb_categories = QComboBox(ImportAccountDialog)
        self.cbb_categories.setObjectName(u"cbb_categories")

        self.horizontalLayout_2.addWidget(self.cbb_categories)

        self.btn_reload = QPushButton(ImportAccountDialog)
        self.btn_reload.setObjectName(u"btn_reload")
        self.btn_reload.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_reload.sizePolicy().hasHeightForWidth())
        self.btn_reload.setSizePolicy(sizePolicy3)
        self.btn_reload.setMinimumSize(QSize(0, 0))
        self.btn_reload.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reload.setStyleSheet(u"QPushButton {\n"
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
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reload.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btn_reload)

        self.btn_delete = QPushButton(ImportAccountDialog)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy1)
        self.btn_delete.setMinimumSize(QSize(0, 0))
        self.btn_delete.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.btn_delete)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.txt_data = QPlainTextEdit(ImportAccountDialog)
        self.txt_data.setObjectName(u"txt_data")
        self.txt_data.setStyleSheet(u"QScrollBar:horizontal {\n"
"    height: 12px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width: 12px;\n"
"}")

        self.verticalLayout.addWidget(self.txt_data)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cbb_data1 = QComboBox(ImportAccountDialog)
        self.cbb_data1.setObjectName(u"cbb_data1")

        self.horizontalLayout.addWidget(self.cbb_data1)

        self.cbb_data2 = QComboBox(ImportAccountDialog)
        self.cbb_data2.setObjectName(u"cbb_data2")

        self.horizontalLayout.addWidget(self.cbb_data2)

        self.cbb_data3 = QComboBox(ImportAccountDialog)
        self.cbb_data3.setObjectName(u"cbb_data3")

        self.horizontalLayout.addWidget(self.cbb_data3)

        self.cbb_data4 = QComboBox(ImportAccountDialog)
        self.cbb_data4.setObjectName(u"cbb_data4")

        self.horizontalLayout.addWidget(self.cbb_data4)

        self.cbb_data5 = QComboBox(ImportAccountDialog)
        self.cbb_data5.setObjectName(u"cbb_data5")

        self.horizontalLayout.addWidget(self.cbb_data5)

        self.cbb_data6 = QComboBox(ImportAccountDialog)
        self.cbb_data6.setObjectName(u"cbb_data6")

        self.horizontalLayout.addWidget(self.cbb_data6)

        self.cbb_data7 = QComboBox(ImportAccountDialog)
        self.cbb_data7.setObjectName(u"cbb_data7")

        self.horizontalLayout.addWidget(self.cbb_data7)

        self.cbb_data8 = QComboBox(ImportAccountDialog)
        self.cbb_data8.setObjectName(u"cbb_data8")

        self.horizontalLayout.addWidget(self.cbb_data8)

        self.cbb_data9 = QComboBox(ImportAccountDialog)
        self.cbb_data9.setObjectName(u"cbb_data9")

        self.horizontalLayout.addWidget(self.cbb_data9)

        self.cbb_data10 = QComboBox(ImportAccountDialog)
        self.cbb_data10.setObjectName(u"cbb_data10")

        self.horizontalLayout.addWidget(self.cbb_data10)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tb_accounts = QTableWidget(ImportAccountDialog)
        if (self.tb_accounts.columnCount() < 10):
            self.tb_accounts.setColumnCount(10)
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
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_accounts.setHorizontalHeaderItem(9, __qtablewidgetitem9)
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
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width: 12px;\n"
"}")
        self.tb_accounts.setFrameShape(QFrame.NoFrame)
        self.tb_accounts.setFrameShadow(QFrame.Sunken)
        self.tb_accounts.setLineWidth(1)
        self.tb_accounts.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tb_accounts.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tb_accounts.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_accounts.setShowGrid(True)
        self.tb_accounts.setGridStyle(Qt.SolidLine)
        self.tb_accounts.setWordWrap(True)
        self.tb_accounts.setCornerButtonEnabled(True)
        self.tb_accounts.setRowCount(0)
        self.tb_accounts.horizontalHeader().setVisible(False)
        self.tb_accounts.horizontalHeader().setCascadingSectionResizes(True)
        self.tb_accounts.horizontalHeader().setMinimumSectionSize(54)
        self.tb_accounts.horizontalHeader().setDefaultSectionSize(200)
        self.tb_accounts.horizontalHeader().setHighlightSections(True)
        self.tb_accounts.horizontalHeader().setProperty("showSortIndicator", True)
        self.tb_accounts.horizontalHeader().setStretchLastSection(True)
        self.tb_accounts.verticalHeader().setVisible(False)
        self.tb_accounts.verticalHeader().setCascadingSectionResizes(False)
        self.tb_accounts.verticalHeader().setProperty("showSortIndicator", False)
        self.tb_accounts.verticalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tb_accounts)

        self.btn_save = QPushButton(ImportAccountDialog)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(0, 30))
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.btn_save)


        self.retranslateUi(ImportAccountDialog)

        QMetaObject.connectSlotsByName(ImportAccountDialog)
    # setupUi

    def retranslateUi(self, ImportAccountDialog):
        ImportAccountDialog.setWindowTitle(QCoreApplication.translate("ImportAccountDialog", u"Dialog", None))
        self.txt_category.setPlaceholderText(QCoreApplication.translate("ImportAccountDialog", u"T\u00ean danh m\u1ee5c", None))
        self.btn_add.setText(QCoreApplication.translate("ImportAccountDialog", u"TH\u00caM", None))
        self.btn_edit.setText(QCoreApplication.translate("ImportAccountDialog", u"S\u1eecA", None))
        self.label.setText(QCoreApplication.translate("ImportAccountDialog", u"Danh m\u1ee5c:", None))
        self.btn_reload.setText("")
        self.btn_delete.setText(QCoreApplication.translate("ImportAccountDialog", u"X\u00d3A", None))
        self.txt_data.setPlaceholderText(QCoreApplication.translate("ImportAccountDialog", u"Nh\u1eadp ds t\u00e0i kho\u1ea3n", None))
        ___qtablewidgetitem = self.tb_accounts.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ImportAccountDialog", u"New Column", None));
        ___qtablewidgetitem1 = self.tb_accounts.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ImportAccountDialog", u"New Column", None));
        ___qtablewidgetitem2 = self.tb_accounts.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ImportAccountDialog", u"New Column", None));
        ___qtablewidgetitem3 = self.tb_accounts.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ImportAccountDialog", u"New Column", None));
        ___qtablewidgetitem4 = self.tb_accounts.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ImportAccountDialog", u"New Column", None));
        ___qtablewidgetitem5 = self.tb_accounts.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ImportAccountDialog", u"New Column", None));
        ___qtablewidgetitem6 = self.tb_accounts.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ImportAccountDialog", u"New Column", None));
        ___qtablewidgetitem7 = self.tb_accounts.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ImportAccountDialog", u"New Column", None));
        ___qtablewidgetitem8 = self.tb_accounts.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("ImportAccountDialog", u"New Column", None));
        ___qtablewidgetitem9 = self.tb_accounts.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("ImportAccountDialog", u"New Column", None));
        self.btn_save.setText(QCoreApplication.translate("ImportAccountDialog", u"L\u01b0u", None))
    # retranslateUi

