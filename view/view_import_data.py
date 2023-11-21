from definitions import ROOT_DIR
from modules import *


class ImportData(QDialog):
    closed = Signal(str)

    def __init__(self, parent=None, data_type="", placeholder=""):
        super(ImportData, self).__init__(parent)
        self.setModal(True)

        self.data_type = data_type

        # THREAD
        self.thread = {}

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_ImportData()
        self.ui.setupUi(self)

        self.thread = {}
        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = f"Thêm danh sách {data_type}"
        # APPLY TEXTS
        self.setWindowTitle(title)
        self.data_save = ""

        try:
            data_file = open(ROOT_DIR + f'/data/{self.data_type}.txt', 'r', encoding='utf-8').read()
            self.ui.txt_data.setPlainText(data_file)
        except:
            pass
        if placeholder:
            self.ui.txt_data.setPlaceholderText(placeholder)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.ui.btn_save.clicked.connect(self.save_data)

        self.show()

    def show_message_dialog(self, icon: QMessageBox.Icon, text):
        msg = QMessageBox(parent=self)
        msg.setIcon(icon)
        msg.setText(text)
        msg.setWindowTitle("Thông báo")
        msg.exec_()

    def save_data(self):
        self.ui.btn_save.setEnabled(False)
        self.data_save = self.ui.txt_data.toPlainText()
        file_save = open(ROOT_DIR + f'/data/{self.data_type}.txt', 'w+', encoding='utf-8')
        file_save.write(self.data_save)
        file_save.close()
        self.ui.btn_save.setEnabled(True)
        self.accept()
