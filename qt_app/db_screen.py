from PyQt6 import QtWidgets
import sys
from qt_app.user_interfaces.sports_interface import Ui_MainWindow


class db_screen(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setup_btns()

    def setup_btns(self):
        self.Hockey.clicked.connect(self.submit)
        self.Football.clicked.connect(self.submit)
        self.Tennis.clicked.connect(self.submit)
        self.Volleyball.clicked.connect(self.submit)
        self.Bascketball.clicked.connect(self.submit)

    def submit(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = db_screen()
    window.show()

    app.exec()
