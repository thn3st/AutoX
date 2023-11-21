from configparser import ConfigParser

import requests

from definitions import ROOT_DIR
from modules import *
from view import ImportData


class SettingDialog(QDialog):
    closed = Signal(str)

    def __init__(self, parent=None):
        super(SettingDialog, self).__init__(parent)
        self.setModal(True)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_SettingDialog()
        self.ui.setupUi(self)

        self.thread = {}
        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = f"Cài đặt"
        # APPLY TEXTS
        self.setWindowTitle(title)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////

        self.ui.btn_save.clicked.connect(self.save_data)
        self.ui.btn_open_list_username_wall.clicked.connect(self.open_list_username_wall)
        self.ui.btn_open_list_username_new_feed.clicked.connect(self.open_list_username_new_feed)

        # SET SETTING SAVE
        try:
            parser = ConfigParser()
            parser.read(ROOT_DIR + '/data/settings.ini')
            is_like_new_feed = parser.get('swipe_new_feed', 'like')
            is_comment_new_feed = parser.get('swipe_new_feed', 'comment')
            is_retweet_new_feed = parser.get('swipe_new_feed', 'retweet')
            is_click_ads_new_feed = parser.get('swipe_new_feed', 'click_ads')
            time_swipe_new_feed = parser.get('swipe_new_feed', 'time_swipe')

            is_like_wall = parser.get('swipe_wall', 'like')
            is_comment_wall = parser.get('swipe_wall', 'comment')
            is_retweet_wall = parser.get('swipe_wall', 'retweet')
            time_swipe_wall = parser.get('swipe_wall', 'time_swipe')

            self.ui.cb_is_like_new_feed.setChecked(is_like_new_feed == '1')
            self.ui.cb_is_comment_new_feed.setChecked(is_comment_new_feed == '1')
            self.ui.cb_is_retweet_new_feed.setChecked(is_retweet_new_feed == '1')
            self.ui.cb_is_click_ads_new_feed.setChecked(is_click_ads_new_feed == '1')
            self.ui.num_time_swipe_new_feed.setValue(int(time_swipe_new_feed))

            self.ui.cb_is_like_wall.setChecked(is_like_wall == '1')
            self.ui.cb_is_comment_wall.setChecked(is_comment_wall == '1')
            self.ui.cb_is_retweet_wall.setChecked(is_retweet_wall == '1')
            self.ui.num_time_swipe_wall.setValue(int(time_swipe_wall))

        except Exception as e:
            self.show_message_dialog(QMessageBox.Warning, 'Vui lòng cập nhật lại file cài đặt !\n' + str(e))

        self.show()

    def show_message_dialog(self, icon: QMessageBox.Icon, text):
        msg = QMessageBox(parent=self)
        msg.setIcon(icon)
        msg.setText(text)
        msg.setWindowTitle("Thông báo")
        msg.exec_()

    def open_list_username_wall(self):
        import_data = ImportData(self, 'list_username_wall')
        import_data.exec_()

    def open_list_username_new_feed(self):
        import_data = ImportData(self, 'list_username_new_feed')
        import_data.exec_()

    def save_data(self):
        is_like_new_feed = self.ui.cb_is_like_new_feed.isChecked()
        is_comment_new_feed = self.ui.cb_is_comment_new_feed.isChecked()
        is_retweet_new_feed = self.ui.cb_is_retweet_new_feed.isChecked()
        is_click_ads_new_feed = self.ui.cb_is_click_ads_new_feed.isChecked()
        time_swipe_new_feed = self.ui.num_time_swipe_new_feed.value()

        is_like_wall = self.ui.cb_is_like_wall.isChecked()
        is_comment_wall = self.ui.cb_is_comment_wall.isChecked()
        is_retweet_wall = self.ui.cb_is_retweet_wall.isChecked()
        time_swipe_wall = self.ui.num_time_swipe_wall.value()

        parser = ConfigParser()

        parser.read(ROOT_DIR + '/data/settings.ini')
        parser.set('swipe_new_feed', 'like', str(int(is_like_new_feed)))
        parser.set('swipe_new_feed', 'comment', str(int(is_comment_new_feed)))
        parser.set('swipe_new_feed', 'retweet', str(int(is_retweet_new_feed)))
        parser.set('swipe_new_feed', 'click_ads', str(int(is_click_ads_new_feed)))
        parser.set('swipe_new_feed', 'time_swipe', str(time_swipe_new_feed))

        parser.set('swipe_wall', 'like', str(int(is_like_wall)))
        parser.set('swipe_wall', 'comment', str(int(is_comment_wall)))
        parser.set('swipe_wall', 'retweet', str(int(is_retweet_wall)))
        parser.set('swipe_new_feed', 'time_swipe', str(time_swipe_wall))

        with open(ROOT_DIR + '/data/settings.ini', 'w') as configfile:
            parser.write(configfile)
        configfile.close()
        self.accept()
