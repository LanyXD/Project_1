from PyQt6.QtWidgets import QApplication
import sys
from main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    app.exec()


main()

