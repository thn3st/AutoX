import queue
import random
import subprocess
from configparser import ConfigParser
from time import sleep

from definitions import ROOT_DIR
from enums import *
import db_account
from PySide2.QtCore import *
import uiautomator2 as u2
from helpers.x_helper import XHelper

CREATE_NO_WINDOW = 0x08000000


class Worker(QThread):
    finished = Signal(object, object)
    emit_tb_accounts = Signal(int, int, object)
    emit_tb_posts = Signal(int, int, object)
    emit_write_logs = Signal(object)

    def __init__(self, ui, data, job_name: JobEnum):
        super(Worker, self).__init__()
        self.device = None
        self.is_running = True
        self.data = data
        self.ui = ui
        self.job_name = job_name

    def send_last_status(self, text, is_save_to_db=True):
        self.emit_tb_accounts.emit(self.device.row, self.ui.tb_accounts.columnCount() - 1, text)
        self.emit_write_logs.emit(f'{self.device.serial} - {text}')
        if is_save_to_db:
            db_account.update_last_status(self.device.serial, text)

    def run(self):
        while self.is_running:
            try:
                self.device = self.data["q_devices"].get(timeout=1)
            except queue.Empty:
                return

            self.send_last_status("kết nối thiết bị ...")
            try:
                d = u2.connect_usb(self.device.serial)
                check = d.info
            except Exception as e:
                self.send_last_status("Lỗi kết nối thiết bị: " + str(e))
                return

            self.send_last_status("kết nối thiết bị thành công")
            x_helper = XHelper(d, self.device, self.data, self.send_last_status)
            if self.job_name == JobEnum.LOGIN_X:
                self.send_last_status("đăng nhập ...")
                if x_helper.login_x():
                    self.send_last_status("đăng nhập thành công")
                else:
                    self.send_last_status("đăng nhập thất bại")

            if self.job_name == JobEnum.SWIPE_NEW_FEED:
                self.send_last_status("lướt newfeed ...")
                x_helper.swipe_new_feed(total_runtime=self.data['time_swipe_new_feed'],
                                        is_random_like=self.data['is_like_new_feed'],
                                        is_random_comment=self.data['is_comment_new_feed'],
                                        is_random_retweet=self.data['is_retweet_new_feed'],
                                        is_click_specify_ads=self.data['is_click_ads_new_feed'])
                self.send_last_status("lướt newfeed xong")

            if self.job_name == JobEnum.SWIPE_WALL:
                self.send_last_status("lướt newfeed ...")
                x_helper.swipe_new_feed(total_runtime=random.randint(20, 40),
                                        is_random_like=self.data['is_like_new_feed'],
                                        is_random_comment=self.data['is_comment_new_feed'],
                                        is_random_retweet=self.data['is_retweet_new_feed'],
                                        is_click_specify_ads=self.data['is_click_ads_new_feed'])
                self.send_last_status("lướt newfeed xong")
                for username in self.data['list_username_wall']:
                    if not username:
                        continue
                    self.send_last_status(f"lướt tường: {username}")
                    x_helper.swipe_wall(username)
                self.send_last_status(f"lướt tường xong")
            if self.job_name == JobEnum.INSTALL_APK:
                for apk in self.data['package_apks']:
                    self.send_last_status(f"cài đặt apk {apk}")
                    d.app_install(ROOT_DIR + f'/data/apk/{apk}.apk')

                self.send_last_status(f"cài đặt apk xong")

            if self.job_name == JobEnum.ADD_PROXY:
                self.send_last_status("thay đổi proxy ...")
                if x_helper.change_proxy():
                    self.send_last_status("thay đổi proxy thành công")
                else:
                    self.send_last_status("thay đổi proxy thất bại")
        return True

    def stop(self):
        self.terminate()

    def check_job_done(self):
        run_count = int(self.ui.txt_running_count.text())
        self.ui.txt_running_count.setText(str(run_count + 1))
        run_all_count = int(self.ui.txt_total_running_count.text())
        if run_count + 1 == run_all_count:
            self.finished.emit("Chương trình đã hoàn thành", True)
