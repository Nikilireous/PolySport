from PyQt6 import QtWidgets
import sys
from qt_app.user_interfaces.sports_interface import Ui_MainWindow
from table_window_screen import TableWindow


class DbScreen(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setup_buttons()
        self.data_existing = True

        try:
            self.tabled_db = TableWindow()

        except FileNotFoundError:
            self.statusbar.setStyleSheet('color: red')
            self.statusbar.showMessage('Database json does not exist')
            self.data_existing = False

    def setup_buttons(self):
        self.Hockey.clicked.connect(self.submit)
        self.Football.clicked.connect(self.submit)
        self.Tennis.clicked.connect(self.submit)
        self.Volleyball.clicked.connect(self.submit)
        self.Bascketball.clicked.connect(self.submit)

    def submit(self):
        if self.sender() == self.Football and self.data_existing:
            self.tabled_db.ui_create()
            self.tabled_db.show()
            self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = DbScreen()
    window.show()

    app.exec()
