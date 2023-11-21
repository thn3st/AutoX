# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingJZrvfj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SettingDialog(object):
    def setupUi(self, SettingDialog):
        if not SettingDialog.objectName():
            SettingDialog.setObjectName(u"SettingDialog")
        SettingDialog.resize(462, 424)
        self.verticalLayout = QVBoxLayout(SettingDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(SettingDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cb_is_comment_new_feed = QCheckBox(self.groupBox)
        self.cb_is_comment_new_feed.setObjectName(u"cb_is_comment_new_feed")

        self.gridLayout.addWidget(self.cb_is_comment_new_feed, 1, 2, 1, 1)

        self.cb_is_retweet_new_feed = QCheckBox(self.groupBox)
        self.cb_is_retweet_new_feed.setObjectName(u"cb_is_retweet_new_feed")

        self.gridLayout.addWidget(self.cb_is_retweet_new_feed, 2, 2, 1, 1)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 2)

        self.btn_open_list_username_new_feed = QPushButton(self.groupBox)
        self.btn_open_list_username_new_feed.setObjectName(u"btn_open_list_username_new_feed")
        self.btn_open_list_username_new_feed.setEnabled(True)
        self.btn_open_list_username_new_feed.setMinimumSize(QSize(0, 20))
        self.btn_open_list_username_new_feed.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open_list_username_new_feed.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.btn_open_list_username_new_feed, 5, 1, 1, 2)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 2)

        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 4, 0, 1, 1)

        self.label_23 = QLabel(self.groupBox)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 3, 0, 1, 1)

        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 1, 0, 1, 2)

        self.num_time_swipe_new_feed = QSpinBox(self.groupBox)
        self.num_time_swipe_new_feed.setObjectName(u"num_time_swipe_new_feed")
        self.num_time_swipe_new_feed.setMaximum(999999999)

        self.gridLayout.addWidget(self.num_time_swipe_new_feed, 4, 1, 1, 2)

        self.cb_is_like_new_feed = QCheckBox(self.groupBox)
        self.cb_is_like_new_feed.setObjectName(u"cb_is_like_new_feed")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_is_like_new_feed.sizePolicy().hasHeightForWidth())
        self.cb_is_like_new_feed.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.cb_is_like_new_feed, 0, 2, 1, 1)

        self.cb_is_click_ads_new_feed = QCheckBox(self.groupBox)
        self.cb_is_click_ads_new_feed.setObjectName(u"cb_is_click_ads_new_feed")

        self.gridLayout.addWidget(self.cb_is_click_ads_new_feed, 3, 2, 1, 1)

        self.label_22 = QLabel(self.groupBox)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 5, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(SettingDialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cb_is_retweet_wall = QCheckBox(self.groupBox_2)
        self.cb_is_retweet_wall.setObjectName(u"cb_is_retweet_wall")

        self.gridLayout_2.addWidget(self.cb_is_retweet_wall, 2, 2, 1, 1)

        self.num_time_swipe_wall = QSpinBox(self.groupBox_2)
        self.num_time_swipe_wall.setObjectName(u"num_time_swipe_wall")
        self.num_time_swipe_wall.setMaximum(999999999)

        self.gridLayout_2.addWidget(self.num_time_swipe_wall, 3, 1, 1, 2)

        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 0, 0, 1, 2)

        self.label_20 = QLabel(self.groupBox_2)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 1, 0, 1, 2)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 2)

        self.cb_is_comment_wall = QCheckBox(self.groupBox_2)
        self.cb_is_comment_wall.setObjectName(u"cb_is_comment_wall")

        self.gridLayout_2.addWidget(self.cb_is_comment_wall, 1, 2, 1, 1)

        self.cb_is_like_wall = QCheckBox(self.groupBox_2)
        self.cb_is_like_wall.setObjectName(u"cb_is_like_wall")
        sizePolicy.setHeightForWidth(self.cb_is_like_wall.sizePolicy().hasHeightForWidth())
        self.cb_is_like_wall.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.cb_is_like_wall, 0, 2, 1, 1)

        self.label_21 = QLabel(self.groupBox_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 3, 0, 1, 1)

        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 4, 0, 1, 1)

        self.btn_open_list_username_wall = QPushButton(self.groupBox_2)
        self.btn_open_list_username_wall.setObjectName(u"btn_open_list_username_wall")
        self.btn_open_list_username_wall.setEnabled(True)
        self.btn_open_list_username_wall.setMinimumSize(QSize(0, 20))
        self.btn_open_list_username_wall.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open_list_username_wall.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_2.addWidget(self.btn_open_list_username_wall, 4, 1, 1, 2)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.btn_save = QPushButton(SettingDialog)
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


        self.retranslateUi(SettingDialog)

        QMetaObject.connectSlotsByName(SettingDialog)
    # setupUi

    def retranslateUi(self, SettingDialog):
        SettingDialog.setWindowTitle(QCoreApplication.translate("SettingDialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingDialog", u"C\u00e0i \u0111\u1eb7t l\u01b0\u1edbt newfeed", None))
        self.cb_is_comment_new_feed.setText("")
        self.cb_is_retweet_new_feed.setText("")
        self.label_15.setText(QCoreApplication.translate("SettingDialog", u"Like:", None))
        self.btn_open_list_username_new_feed.setText(QCoreApplication.translate("SettingDialog", u"M\u1ede", None))
        self.label_10.setText(QCoreApplication.translate("SettingDialog", u"Retweet:", None))
        self.label_18.setText(QCoreApplication.translate("SettingDialog", u"Th\u1eddi gian l\u01b0\u1edbt:", None))
        self.label_23.setText(QCoreApplication.translate("SettingDialog", u"B\u1eaft c\u00e1o: ", None))
        self.label_19.setText(QCoreApplication.translate("SettingDialog", u"B\u00ecnh lu\u1eadn:", None))
        self.cb_is_like_new_feed.setText("")
        self.cb_is_click_ads_new_feed.setText("")
        self.label_22.setText(QCoreApplication.translate("SettingDialog", u"DS username:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SettingDialog", u"C\u00e0i \u0111\u1eb7t t\u01b0\u01a1ng t\u00e1c t\u01b0\u1eddng", None))
        self.cb_is_retweet_wall.setText("")
        self.label_16.setText(QCoreApplication.translate("SettingDialog", u"Like:", None))
        self.label_20.setText(QCoreApplication.translate("SettingDialog", u"B\u00ecnh lu\u1eadn:", None))
        self.label_11.setText(QCoreApplication.translate("SettingDialog", u"Retweet:", None))
        self.cb_is_comment_wall.setText("")
        self.cb_is_like_wall.setText("")
        self.label_21.setText(QCoreApplication.translate("SettingDialog", u"Th\u1eddi gian l\u01b0\u1edbt:", None))
        self.label_17.setText(QCoreApplication.translate("SettingDialog", u"DS username:", None))
        self.btn_open_list_username_wall.setText(QCoreApplication.translate("SettingDialog", u"M\u1ede", None))
        self.btn_save.setText(QCoreApplication.translate("SettingDialog", u"L\u01afU", None))
    # retranslateUi

