from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from log_window import Ui_MainWindow


class login_window(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setup_btns()

        self.password = "password"
        self.login = "login"

    def setup_btns(self):
        self.submit_btn.clicked.connect(self.submit)

    def submit(self):
        text_login = self.login_edit.toPlainText()
        text_password = self.password_edit.toPlainText()

        if text_login == self.login and text_password == self.password:
            print(1)
        else:
            self.statusBar.showMessage("You are fucking idiot")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = login_window()
    window.show()

    app.exec()
