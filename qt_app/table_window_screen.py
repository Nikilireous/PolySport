from PyQt6 import QtWidgets
import sys

from PyQt6.QtWidgets import QLabel

from qt_app.user_interfaces.table_window_interface import Ui_MainWindow
import json


class TableWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.correct_table = 'awards'

        self.file = open('json_files/database.json', 'r')
        self.data = json.load(self.file)

        for key in sorted(list(self.data.keys())):
            self.comboBox.addItem(key)

        self.mainTable.cellDoubleClicked.connect(self.change_table)
        self.comboBox.currentTextChanged.connect(self.box_change)

        self.team_words = ['team_name', 'team_id', 'team1_id', 'team2_id', 'winner_team_id', 'champion_team_id']
        self.game_words = ['game_id']
        self.judge_words = ['judge_id']
        self.season_words = ['season_id']

    def ui_create(self) -> None:
        self.mainTable.clear()
        data = self.data[self.correct_table]
        self.mainTable.setRowCount(len(data))
        self.mainTable.setColumnCount(len(data[0]))
        self.mainTable.setHorizontalHeaderLabels(list(map(lambda x: x.capitalize().replace('_', ' '),
                                                          (data[0].keys()))))

        for x_coord, row in enumerate(data):
            for y_coord, cell in enumerate(row.values()):
                label = QLabel()
                label.setStyleSheet('color: black')
                label.setText(str(cell))

                self.mainTable.setCellWidget(x_coord, y_coord, label)
        self.mainTable.resizeColumnsToContents()

    def change_table(self, x, y):
        data = self.data[self.correct_table]
        changing = list(data[0].keys())[y]
        print(changing)

        if str(changing) in self.team_words:
            self.correct_table = 'teams'

        elif str(changing) in self.game_words:
            self.correct_table = 'games'

        elif str(changing) in self.judge_words:
            self.correct_table = 'judges'

        elif str(changing) in self.season_words:
            self.correct_table = 'seasons'

        self.ui_create()


    def box_change(self):
        self.correct_table = self.comboBox.currentText()
        self.ui_create()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    try:
        window = TableWindow()
        window.ui_create()

        window.show()
        app.exec()

    except FileNotFoundError:
        pass
