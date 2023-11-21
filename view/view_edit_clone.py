import db_account
from modules import *


class EditCloneDialog(QDialog):
    closed = Signal(str)

    def __init__(self, parent=None, list_uid=None, is_multiple=False):
        super(EditCloneDialog, self).__init__(parent)
        if list_uid is None:
            list_uid = []
        self.is_multiple = len(list_uid) > 1
        self.setModal(True)
        self.list_uid = list_uid

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_EditCloneDialog()
        self.ui.setupUi(self)

        self.thread = {}
        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = f"Edit clone"
        # APPLY TEXTS
        self.setWindowTitle(title)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.ui.btn_save.clicked.connect(self.save_data)

        self.ui.cbb_categories.clear()
        categories = [s[0] for s in db_account.get_all_category()]
        self.ui.cbb_categories.addItems(categories)

        # SET CLONE
        if not self.is_multiple:
            clone = db_account.get_account_to_model(self.list_uid[0])
            self.ui.txt_uid.setText(clone.uid)
            self.ui.txt_password.setText(clone.password)
            self.ui.txt_2fa.setText(clone.two_fa)
            self.ui.txt_token.setText(clone.token)
            self.ui.txt_cookie.setText(clone.cookie)
            self.ui.txt_mail.setText(clone.mail)
            self.ui.txt_pass_mail.setText(clone.pass_mail)
            self.ui.txt_ua.setText(clone.ua)
            self.ui.cbb_categories.setCurrentText(clone.category_name)
        else:
            self.ui.txt_password.setText('DONT_CHANGE')
            self.ui.txt_pass_mail.setText('DONT_CHANGE')
            self.ui.txt_ua.setText('DONT_CHANGE')
            self.ui.txt_2fa.setEnabled(False)
            self.ui.txt_uid.setEnabled(False)
            self.ui.txt_token.setEnabled(False)
            self.ui.txt_mail.setEnabled(False)
            self.ui.txt_cookie.setEnabled(False)
            self.ui.txt_mail.setEnabled(False)

        self.show()

    def show_message_dialog(self, icon: QMessageBox.Icon, text):
        msg = QMessageBox(parent=self)
        msg.setIcon(icon)
        msg.setText(text)
        msg.setWindowTitle("Thông báo")
        msg.exec_()

    def save_data(self):
        category_id = db_account.search_category_by_name(self.ui.cbb_categories.currentText())[0]
        if self.is_multiple:
            password = self.ui.txt_password.text()
            pass_mail = self.ui.txt_pass_mail.text()
            ua = self.ui.txt_ua.text()
            if password == "DONT_CHANGE":
                password = None
            if pass_mail == "DONT_CHANGE":
                pass_mail = None
            if ua == "DONT_CHANGE":
                ua = None
            db_account.update_accounts(self.list_uid, pass_mail=pass_mail, new_password=password, ua=ua, category_id=category_id)
        else:
            uid = self.ui.txt_uid.text()
            password = self.ui.txt_password.text()
            two_fa = self.ui.txt_2fa.text()
            token = self.ui.txt_token.text()
            cookie = self.ui.txt_cookie.text()
            mail = self.ui.txt_mail.text()
            pass_mail = self.ui.txt_pass_mail.text()
            ua = self.ui.txt_ua.text()
            db_account.update_account(uid, new_password=password, two_fa=two_fa, token=token, cookie=cookie,
                                      mail=mail, pass_mail=pass_mail, ua=ua, category_id=category_id)
        self.accept()
