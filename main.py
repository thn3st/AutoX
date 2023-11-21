import queue
import random
import sys
import os
from datetime import datetime

import adbutils
import pyperclip
from definitions import ROOT_DIR
from enums import JobEnum
from helpers.get_data_setting_file import GetConfigSetting
from models.device import DevicePhone
from modules import *
from view import *
import db_account
from worker import Worker

VERSION = "1.0.0"


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # CONNECT DB
        db_account.create_table()

        # KEY
        self.is_active_key = True

        # THREAD
        self.thread = {}

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = f"AUTO X - Kiếm tiền nhanh như X"
        # APPLY TEXTS
        self.setWindowTitle(title)

        widgets.txt_version.setText(VERSION)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////\
        widgets.btn_open_setting.clicked.connect(self.open_settings)
        widgets.btn_import_devices.clicked.connect(self.import_devices)

        # EDIT TABLE
        widgets.tb_accounts.setColumnWidth(0, 50)
        widgets.tb_accounts.setColumnWidth(1, 150)
        widgets.tb_accounts.setColumnWidth(2, 100)
        widgets.tb_accounts.setColumnWidth(8, 80)
        widgets.tb_accounts.setColumnWidth(9, 80)
        widgets.tb_accounts.setColumnWidth(10, 80)
        widgets.tb_accounts.setColumnWidth(12, 80)
        widgets.tb_accounts.setColumnWidth(13, 80)
        widgets.tb_accounts.setColumnWidth(14, 80)
        widgets.tb_accounts.setColumnWidth(15, 80)
        widgets.tb_accounts.setColumnWidth(16, 80)
        widgets.tb_accounts.setColumnWidth(widgets.tb_accounts.columnCount() - 1, 600)
        widgets.tb_accounts.verticalHeader().setStretchLastSection(False)
        widgets.tb_accounts.setSortingEnabled(False)
        self.reload_table_accounts()

        # ON SELECTED ROW TABLE CLONES
        widgets.tb_accounts.selectionModel().selectionChanged.connect(
            lambda: widgets.txt_selected_count.setText(str(len(widgets.tb_accounts.selectionModel().selectedRows()))))

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.showMaximized()

    # WRITE LOGS TO APP
    def write_logs(self,  content):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        self.ui.txt_logs.insertPlainText(f'{dt_string} | {content} \n')

    def open_settings(self):
        setting_dialog = SettingDialog(self)
        setting_dialog.exec_()

    # RIGHT CLICK TABLE
    def contextMenuEvent(self, pos):
        if widgets.tb_accounts.selectionModel().selectedRows():
            list_selected_row = [index.row() for index in widgets.tb_accounts.selectionModel().selectedRows()]
            menu = QMenu()

            login_x = menu.addAction("Login X")

            swipe_new_feed = menu.addAction("Lướt newfeed")

            swipe_wall = menu.addAction("Tương tác tường")

            change_proxy = menu.addAction("Thay đổi proxy")

            install_apk = menu.addAction("Cài đặt apk")

            stop_device = menu.addAction("Dừng")

            add_account = menu.addAction("Thêm tài khoản")

            copy_to_clipboard = menu.addAction("Copy tài khoản vào clipboard")

            delete_selected_rows = menu.addAction("Xoá thiết bị")

            menu.popup(QCursor.pos())
            action = menu.exec_()

            if not action:
                return

            if action in [change_proxy, login_x, swipe_new_feed, swipe_wall, install_apk]:
                settings_x = GetConfigSetting.get_config_x()
                package_apks = []
                job_name = None
                if action == change_proxy:
                    job_name = JobEnum.ADD_PROXY
                elif action == login_x:
                    job_name = JobEnum.LOGIN_X
                elif action == swipe_new_feed:
                    job_name = JobEnum.SWIPE_NEW_FEED
                elif action == swipe_wall:
                    job_name = JobEnum.SWIPE_WALL
                elif action == install_apk:
                    import_data = ImportData(self, 'package apk', 'Package apk')
                    result = import_data.exec_()
                    if result == 0:
                        return
                    package_apks = import_data.data_save.split("\n")
                    job_name = JobEnum.INSTALL_APK

                settings_x['package_apks'] = package_apks
                q_devices = queue.Queue()
                list_serial = [widgets.tb_accounts.item(row, 1).text() for row in list_selected_row]
                list_device = db_account.get_account_to_models(list_serial)
                with open(ROOT_DIR + '/data/list_username_new_feed.txt', 'r', encoding='utf-8') as file_username_new_feed:
                    list_username_new_feed = file_username_new_feed.read().split('\n')

                with open(ROOT_DIR + '/data/list_username_wall.txt', 'r', encoding='utf-8') as file_username_wall:
                    list_username_wall = file_username_wall.read().split('\n')

                sorted_list_device = sorted(list_device, key=lambda item: list_serial.index(
                    item.serial) if item.serial in list_serial else len(list_serial))

                for index, device in enumerate(sorted_list_device):
                    device.row = list_selected_row[list_serial.index(device.serial)]
                    q_devices.put_nowait(device)

                settings_x['q_devices'] = q_devices
                settings_x['list_username_new_feed'] = list_username_new_feed
                settings_x['list_username_wall'] = list_username_wall
                for thread_index in range(len(list_selected_row)):
                    serial = widgets.tb_accounts.item(list_selected_row[thread_index], 1).text()
                    self.thread[f'{serial}'] = Worker(widgets, settings_x, job_name=job_name)
                    self.thread[f'{serial}'].emit_tb_accounts.connect(self.connect_tb_accounts)
                    self.thread[f'{serial}'].emit_write_logs.connect(self.write_logs)
                    self.thread[f'{serial}'].finished.connect(self.show_message_dialog_text)
                    self.thread[f'{serial}'].start()

            if action == stop_device:
                list_serial = [widgets.tb_accounts.item(row, 1).text() for row in list_selected_row]
                for row in list_selected_row:
                    self.connect_tb_accounts(row, widgets.tb_accounts.columnCount() - 1, "Dừng")
                for serial in list_serial:
                    try:
                        self.thread[f'{serial}'].stop()
                    except:
                        pass

            if action == delete_selected_rows:
                ret = QMessageBox.question(self, 'Cảnh báo', "Bạn có muốn xóa các tài khoản đã chọn ?",
                                           QMessageBox.No | QMessageBox.Yes)
                if ret == QMessageBox.Yes:
                    list_uid = [str(widgets.tb_accounts.item(row, 1).text()) for row in list_selected_row]
                    db_account.delete_device_by_serials(list_uid)
                    self.reload_table_accounts()
                    return

            if action == copy_to_clipboard:
                self.copy_to_clipboard()
                return

            if action == add_account:
                import_data = ImportData(self, 'account_x', 'user_name|pass|2fa|mail|pass_mail|proxy')
                result = import_data.exec_()
                if result == 0:
                    return
                for index, account in enumerate(import_data.data_save.split('\n')):
                    if not account:
                        continue
                    mail, pass_mail, password, user_name, two_fa, proxy = account.split("|")
                    try:
                        serial = str(widgets.tb_accounts.item(list_selected_row[index], 1).text())
                        device = db_account.find_device_by_serial(serial)
                        device.user_name = user_name
                        device.password = password
                        device.two_fa = two_fa
                        device.mail = mail
                        device.pass_mail = pass_mail
                        device.proxy = proxy
                        db_account.update_device(device)
                    except:
                        break
                self.reload_table_accounts()

    def show_message_dialog(self, icon: QMessageBox.Icon, text=""):
        msg = QMessageBox(parent=self)
        msg.setIcon(icon)
        msg.setText(text)
        msg.setWindowTitle("Thông báo")
        msg.exec_()

    def copy_to_clipboard(self):
        content_copy = ''
        for index in widgets.tb_accounts.selectionModel().selectedRows():
            serial = widgets.tb_accounts.item(index.row(), 1).text()
            account = db_account.get_account_to_save(serial)
            if account is None:
                continue
            data_save = ""
            for data in account:
                if data is None:
                    data_save += "|"
                else:
                    data_save += data + "|"
            content_copy += data_save + "\n"
        pyperclip.copy(content_copy)
        self.show_message_dialog_text("Copied to clipboard")

    def show_message_dialog_text(self, text="", is_finished=False):
        msg = QMessageBox(parent=self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.setWindowTitle("Thông báo")
        msg.exec_()

    def connect_tb_accounts(self, row, column, text):
        if type(text) == int:
            item = QTableWidgetItem()
            item.setData(Qt.DisplayRole, text)
            self.ui.tb_accounts.setItem(row, column, item)
        else:
            item = QTableWidgetItem(str(text))
            self.ui.tb_accounts.setItem(row, column, item)

    def stop(self):
        for thread in self.thread:
            self.thread[thread].stop()

    def reload_table_accounts(self):
        widgets.tb_accounts.setRowCount(0)
        devices = db_account.find_all_devices()
        for device in devices:
            row = widgets.tb_accounts.rowCount()
            widgets.tb_accounts.insertRow(row)
            self.connect_tb_accounts(row, 0, row + 1)
            self.connect_tb_accounts(row, 1, device.serial)
            self.connect_tb_accounts(row, 2, device.user_name)
            self.connect_tb_accounts(row, 3, device.password)
            self.connect_tb_accounts(row, 4, device.two_fa)
            self.connect_tb_accounts(row, 5, device.mail)
            self.connect_tb_accounts(row, 6, device.pass_mail)
            self.connect_tb_accounts(row, 7, device.proxy)
        widgets.txt_total_count.setText(str(len(devices)))

    def import_devices(self):
        _devices = adbutils.AdbClient().device_list()
        devices = []
        for _device in _devices:
            device = DevicePhone()
            device.serial = _device.serial
            devices.append(device)
        db_account.save_devices(devices)
        self.reload_table_accounts()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
