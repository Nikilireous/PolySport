from PyQt6 import QtWidgets
import sys
from qt_app.user_interfaces.log_interface import Ui_MainWindow
from db_screen import db_screen


class login_window(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setup_btns()

        self.password = "password"
        self.login = "login"
        self.second_screen = db_screen()

    def setup_btns(self):
        self.submit_btn.clicked.connect(self.submit)

    def submit(self):
        text_login = self.login_edit.toPlainText()
        text_password = self.password_edit.toPlainText()

        if text_login == self.login and text_password == self.password:
            self.second_screen.show()
            self.close()
        else:
            self.statusBar.showMessage("No no no mister fish, you won't still our db")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = login_window()
    window.show()

    app.exec()
