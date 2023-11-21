# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_accountyTxjAU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_EditAccountDialog(object):
    def setupUi(self, EditAccountDialog):
        if not EditAccountDialog.objectName():
            EditAccountDialog.setObjectName(u"EditAccountDialog")
        EditAccountDialog.resize(980, 285)
        self.verticalLayout = QVBoxLayout(EditAccountDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setContentsMargins(-1, 0, -1, 5)
        self.label = QLabel(EditAccountDialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_8 = QLabel(EditAccountDialog)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.txt_password = QLineEdit(EditAccountDialog)
        self.txt_password.setObjectName(u"txt_password")

        self.gridLayout.addWidget(self.txt_password, 1, 3, 1, 1)

        self.label_3 = QLabel(EditAccountDialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_6 = QLabel(EditAccountDialog)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_9 = QLabel(EditAccountDialog)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)

        self.txt_username = QLineEdit(EditAccountDialog)
        self.txt_username.setObjectName(u"txt_username")
        self.txt_username.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_username, 0, 3, 1, 1)

        self.cbb_categories = QComboBox(EditAccountDialog)
        self.cbb_categories.setObjectName(u"cbb_categories")

        self.gridLayout.addWidget(self.cbb_categories, 6, 3, 1, 1)

        self.label_5 = QLabel(EditAccountDialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.txt_2fa = QLineEdit(EditAccountDialog)
        self.txt_2fa.setObjectName(u"txt_2fa")

        self.gridLayout.addWidget(self.txt_2fa, 2, 3, 1, 1)

        self.txt_mail = QLineEdit(EditAccountDialog)
        self.txt_mail.setObjectName(u"txt_mail")

        self.gridLayout.addWidget(self.txt_mail, 3, 3, 1, 1)

        self.txt_pass_mail = QLineEdit(EditAccountDialog)
        self.txt_pass_mail.setObjectName(u"txt_pass_mail")

        self.gridLayout.addWidget(self.txt_pass_mail, 5, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.btn_save = QPushButton(EditAccountDialog)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setEnabled(True)
        self.btn_save.setMinimumSize(QSize(0, 40))
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

        self.horizontalLayout.addWidget(self.btn_save)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(EditAccountDialog)

        QMetaObject.connectSlotsByName(EditAccountDialog)
    # setupUi

    def retranslateUi(self, EditAccountDialog):
        EditAccountDialog.setWindowTitle(QCoreApplication.translate("EditAccountDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("EditAccountDialog", u"Username:", None))
        self.label_8.setText(QCoreApplication.translate("EditAccountDialog", u"2FA", None))
        self.label_3.setText(QCoreApplication.translate("EditAccountDialog", u"Password:", None))
        self.label_6.setText(QCoreApplication.translate("EditAccountDialog", u"Password Mail:", None))
        self.label_9.setText(QCoreApplication.translate("EditAccountDialog", u"Danh m\u1ee5c:", None))
        self.label_5.setText(QCoreApplication.translate("EditAccountDialog", u"Mail:", None))
        self.btn_save.setText(QCoreApplication.translate("EditAccountDialog", u"L\u01afU", None))
    # retranslateUi

