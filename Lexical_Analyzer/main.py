from PyQt6.QtWidgets import QApplication
import sys
from mainwindow import MainWindow

app = QApplication(sys.argv)
win = MainWindow()


def main():
    win.show()
    app.exec()


main()
