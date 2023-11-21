# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'import_datakYcKBf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_ImportData(object):
    def setupUi(self, ImportData):
        if not ImportData.objectName():
            ImportData.setObjectName(u"ImportData")
        ImportData.resize(804, 353)
        self.verticalLayout = QVBoxLayout(ImportData)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txt_data = QPlainTextEdit(ImportData)
        self.txt_data.setObjectName(u"txt_data")
        self.txt_data.setStyleSheet(u"QScrollBar:horizontal {\n"
"    height: 12px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width: 12px;\n"
"}")

        self.verticalLayout.addWidget(self.txt_data)

        self.btn_save = QPushButton(ImportData)
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


        self.retranslateUi(ImportData)

        QMetaObject.connectSlotsByName(ImportData)
    # setupUi

    def retranslateUi(self, ImportData):
        ImportData.setWindowTitle(QCoreApplication.translate("ImportData", u"Dialog", None))
        self.txt_data.setPlaceholderText(QCoreApplication.translate("ImportData", u"Nh\u1eadp ds data, m\u1ed7i data 1 d\u00f2ng", None))
        self.btn_save.setText(QCoreApplication.translate("ImportData", u"L\u01b0u", None))
    # retranslateUi

