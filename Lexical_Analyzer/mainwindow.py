from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QToolBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 500)
        self.setWindowTitle("Analizador")

        toolbar = QToolBar("toolbar")
        self.addToolBar(toolbar)

        button_action1 = QAction("Cargar", self)
        button_action1.setStatusTip("Cargar un archivo de texto")
        toolbar.addAction(button_action1)

        button_action2 = QAction("Analizar", self)
        button_action2.setStatusTip("Analiza el archivo cargado")
        toolbar.addAction(button_action2)
