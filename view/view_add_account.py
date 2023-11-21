import random
from configparser import ConfigParser

from definitions import ROOT_DIR
from modules import *

CREATE_NO_WINDOW = 0x08000000
import db_account


class ImportClones(QDialog):
    closed = Signal(str)

    def __init__(self, parent=None):
        super(ImportClones, self).__init__(parent)
        self.setModal(True)

        # THREAD
        self.thread = {}

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_ImportClones()
        self.ui.setupUi(self)

        self.thread = {}
        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Thêm tài khoản"
        # APPLY TEXTS
        self.setWindowTitle(title)

        ## ADD DATA COMBOBOX
        self.ui.cbb_data1.addItems(
            ['', 'uid', 'password', '2fa', 'cookie', 'token', 'mail', 'pass_mail', 'ua', 'ua_2fa', 'birthday', 'proxy', 'secondary_mail'])
        self.ui.cbb_data2.addItems(
            ['', 'uid', 'password', '2fa', 'cookie', 'token', 'mail', 'pass_mail', 'ua', 'ua_2fa', 'birthday', 'proxy', 'secondary_mail'])
        self.ui.cbb_data3.addItems(
            ['', 'uid', 'password', '2fa', 'cookie', 'token', 'mail', 'pass_mail', 'ua', 'ua_2fa', 'birthday', 'proxy', 'secondary_mail'])
        self.ui.cbb_data4.addItems(
            ['', 'uid', 'password', '2fa', 'cookie', 'token', 'mail', 'pass_mail', 'ua', 'ua_2fa', 'birthday', 'proxy', 'secondary_mail'])
        self.ui.cbb_data5.addItems(
            ['', 'uid', 'password', '2fa', 'cookie', 'token', 'mail', 'pass_mail', 'ua', 'ua_2fa', 'birthday', 'proxy', 'secondary_mail'])
        self.ui.cbb_data6.addItems(
            ['', 'uid', 'password', '2fa', 'cookie', 'token', 'mail', 'pass_mail', 'ua', 'ua_2fa', 'birthday', 'proxy', 'secondary_mail'])
        self.ui.cbb_data7.addItems(
            ['', 'uid', 'password', '2fa', 'cookie', 'token', 'mail', 'pass_mail', 'ua', 'ua_2fa', 'birthday', 'proxy', 'secondary_mail'])
        self.ui.cbb_data8.addItems(
            ['', 'uid', 'password', '2fa', 'cookie', 'token', 'mail', 'pass_mail', 'ua', 'ua_2fa', 'birthday', 'proxy', 'secondary_mail'])
        self.ui.cbb_data9.addItems(
            ['', 'uid', 'password', '2fa', 'cookie', 'token', 'mail', 'pass_mail', 'ua', 'ua_2fa', 'birthday', 'proxy', 'secondary_mail'])
        self.ui.cbb_data10.addItems(
            ['', 'uid', 'password', '2fa', 'cookie', 'token', 'mail', 'pass_mail', 'ua', 'ua_2fa', 'birthday', 'proxy', 'secondary_mail'])

        header = self.ui.tb_clones.horizontalHeader()
        for i in range(self.ui.tb_clones.columnCount()):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////
        self.ui.cbb_categories.activated.connect(lambda: self.set_category_name())
        self.ui.btn_reload.clicked.connect(self.reload_categories)
        self.ui.btn_add.clicked.connect(self.add_category)
        self.ui.btn_delete.clicked.connect(self.delete_category)
        self.ui.btn_save.clicked.connect(self.save_account)
        self.ui.btn_edit.clicked.connect(self.edit_category)
        self.ui.txt_data.textChanged.connect(self.add_account_table)
        self.reload_categories()

        self.ui.tb_clones.verticalHeader().setStretchLastSection(False)

        # SETUP SETTINGS
        try:
            parser = ConfigParser()
            parser.read(ROOT_DIR + '/data/settings.ini')
            import_clones = parser.get('import', 'clones').split('|')
            self.ui.cbb_data1.setCurrentText(import_clones[0])
            self.ui.cbb_data2.setCurrentText(import_clones[1])
            self.ui.cbb_data3.setCurrentText(import_clones[2])
            self.ui.cbb_data4.setCurrentText(import_clones[3])
            self.ui.cbb_data5.setCurrentText(import_clones[4])
            self.ui.cbb_data6.setCurrentText(import_clones[5])
            self.ui.cbb_data7.setCurrentText(import_clones[6])
            self.ui.cbb_data8.setCurrentText(import_clones[7])
            self.ui.cbb_data9.setCurrentText(import_clones[8])
            self.ui.cbb_data10.setCurrentText(import_clones[9])
        except:
            pass
        # SHOW APP
        # ///////////////////////////////////////////////////////////////

        self.show()

    def show_message_dialog(self, icon: QMessageBox.Icon, text):
        msg = QMessageBox(parent=self)
        msg.setIcon(icon)
        msg.setText(text)
        msg.setWindowTitle("Thông báo")
        msg.exec_()

    def reload_categories(self):
        self.ui.cbb_categories.clear()
        self.ui.cbb_categories.addItem("")
        categories = [s[0] for s in db_account.get_all_category()]
        self.ui.cbb_categories.addItems(categories)

    def set_category_name(self):
        category = self.ui.cbb_categories.currentText()
        if category != "":
            self.ui.txt_category.setText(category)

    def edit_category(self):
        category_new = self.ui.txt_category.text()
        category_old = self.ui.cbb_categories.currentText()
        if db_account.update_category_name(category_new, category_old):
            self.show_message_dialog(QMessageBox.Information, "Sửa danh mục thành công")
            self.reload_categories()
            self.ui.cbb_categories.setCurrentText(category_new)
        else:
            self.show_message_dialog(QMessageBox.Warning, "Sửa danh mục thất bại")

    def add_account_table(self):
        self.ui.tb_clones.setRowCount(0)
        list_account_add = self.ui.txt_data.toPlainText().split('\n')
        for account_add in list_account_add:
            account_add = account_add.replace("v1|3", "v1.3")
            if not account_add or account_add is None:
                continue
            row = self.ui.tb_clones.rowCount()
            self.ui.tb_clones.insertRow(row)
            data_add = account_add.split('|')
            for i in range(len(data_add)):
                self.ui.tb_clones.setItem(row, i, QTableWidgetItem(data_add[i]))

    def add_category(self):
        category = self.ui.txt_category.text()
        if category == "":
            self.show_message_dialog(QMessageBox.Warning, "Vui lòng điền tên danh mục")
            self.ui.txt_category.setFocus()
            return
        if db_account.add_category(category):
            self.show_message_dialog(QMessageBox.Information, "Thêm danh mục thành công")
        else:
            self.show_message_dialog(QMessageBox.Warning, "Thêm danh mục thất bại")

        self.reload_categories()
        self.ui.cbb_categories.setCurrentText(category)

    def delete_category(self):
        category = self.ui.cbb_categories.currentText()
        if category == "":
            self.show_message_dialog(QMessageBox.Warning, "Vui lòng điền tên danh mục")
            self.ui.txt_category.setFocus()
            return
        ret = QMessageBox.question(self, 'Cảnh báo', "Bạn sẽ xóa tất cả các tài khoản trong danh mục này ?",
                                   QMessageBox.No | QMessageBox.Yes)
        if ret == QMessageBox.Yes:
            if db_account.delete_category_by_name(category):
                self.show_message_dialog(QMessageBox.Information, "'Xóa danh mục thành công")
            else:
                self.show_message_dialog(QMessageBox.Warning, "Xóa danh mục thất bại")
        self.reload_categories()

    def save_account(self):
        list_proxy = open(ROOT_DIR + '\\data\\proxies.txt', 'r', encoding='utf-8').read().split('\n')
        try:
            list_proxy.remove('')
        except:
            pass
        try:
            import_clones = self.ui.cbb_data1.currentText() + "|" + self.ui.cbb_data2.currentText() + "|" + \
                            self.ui.cbb_data3.currentText() + "|" + self.ui.cbb_data4.currentText() + "|" + \
                            self.ui.cbb_data5.currentText() + "|" + self.ui.cbb_data6.currentText() + "|" + \
                            self.ui.cbb_data7.currentText() + "|" + self.ui.cbb_data8.currentText() + "|" + \
                            self.ui.cbb_data9.currentText() + "|" + self.ui.cbb_data10.currentText() + "|"
            parser = ConfigParser()
            parser.read(ROOT_DIR + '/data/settings.ini')
            parser.set('import', 'clones', import_clones)
            with open(ROOT_DIR + '/data/settings.ini', 'w') as configfile:
                parser.write(configfile)
            configfile.close()
        except:
            pass
        category = self.ui.cbb_categories.currentText()
        if category == "":
            self.show_message_dialog(QMessageBox.Warning, "Vui lòng điền tên danh mục")
            self.ui.txt_category.setFocus()
            return
        row_count = self.ui.tb_clones.rowCount()
        list_query = []
        list_value = []
        self.ui.btn_save.setEnabled(False)
        for row in range(row_count):
            query = "INSERT INTO ACCOUNT ("
            value = " VALUES ("
            data_value = ()
            if self.ui.cb_rd_proxy_clone.isChecked():
                query += "PROXY, "
                value += "?,"
                data_value = (*data_value, random.choice(list_proxy))
            if self.ui.cbb_data1.currentText() != "":
                query += self.ui.cbb_data1.currentText() + ", "
                value += "?,"
                try:
                    text = self.ui.tb_clones.item(row, 0).text()
                except:
                    text = ""
                data_value = (*data_value, text)
            if self.ui.cbb_data2.currentText() != "":
                query += self.ui.cbb_data2.currentText() + ", "
                value += "?,"
                try:
                    text = self.ui.tb_clones.item(row, 1).text()
                except:
                    text = ""
                data_value = (*data_value, text)
            if self.ui.cbb_data3.currentText() != "":
                query += self.ui.cbb_data3.currentText() + ", "
                value += "?,"
                try:
                    text = self.ui.tb_clones.item(row, 2).text()
                except:
                    text = ""
                data_value = (*data_value, text)
            if self.ui.cbb_data4.currentText() != "":
                query += self.ui.cbb_data4.currentText() + ", "
                value += "?,"
                try:
                    text = self.ui.tb_clones.item(row, 3).text()
                except:
                    text = ""
                data_value = (*data_value, text)
            if self.ui.cbb_data5.currentText() != "":
                query += self.ui.cbb_data5.currentText() + ", "
                value += "?,"
                try:
                    text = self.ui.tb_clones.item(row, 4).text()
                except:
                    text = ""
                data_value = (*data_value, text)
            if self.ui.cbb_data6.currentText() != "":
                query += self.ui.cbb_data6.currentText() + ", "
                value += "?,"
                try:
                    text = self.ui.tb_clones.item(row, 5).text()
                except:
                    text = ""
                data_value = (*data_value, text)
            if self.ui.cbb_data7.currentText() != "":
                query += self.ui.cbb_data7.currentText() + ", "
                value += "?,"
                try:
                    text = self.ui.tb_clones.item(row, 6).text()
                except:
                    text = ""
                data_value = (*data_value, text)
            if self.ui.cbb_data8.currentText() != "":
                query += self.ui.cbb_data8.currentText() + ", "
                value += "?,"
                try:
                    text = self.ui.tb_clones.item(row, 7).text()
                except:
                    text = ""
                data_value = (*data_value, text)
            if self.ui.cbb_data9.currentText() != "":
                query += self.ui.cbb_data9.currentText() + ", "
                value += "?,"
                try:
                    text = self.ui.tb_clones.item(row, 8).text()
                except:
                    text = ""
                data_value = (*data_value, text)
            if self.ui.cbb_data10.currentText() != "":
                query += self.ui.cbb_data10.currentText() + ", "
                value += "?,"
                try:
                    text = self.ui.tb_clones.item(row, 9).text()
                except:
                    text = ""
                data_value = (*data_value, text)

            category_id = db_account.search_category_by_name(category)[0]
            query += "CATEGORY, STATUS)"
            value += "?, ?)"
            data_value = (*data_value, category_id, "956_CP")
            list_query.append(query.replace("ua_2fa", "ua_twofa").replace("2fa", "twofa") + value)
            list_value.append(data_value)
        result = db_account.add_accounts(list_query, list_value)
        self.show_message_dialog(QMessageBox.Information,
                                 f"Thêm {str(result['success_count'])} thành công và {str(result['fail_count'])} thất bại")
        self.ui.btn_save.setEnabled(True)
        return

