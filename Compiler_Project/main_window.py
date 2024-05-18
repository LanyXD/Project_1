from PyQt6.QtWidgets import \
    QMainWindow, \
    QToolBar, \
    QVBoxLayout, \
    QHBoxLayout
from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_window()
        self.show()

    def initialize_window(self):
        self.setFixedSize(800, 600)
        self.setWindowTitle("Analizador")

        self.window_builder()

    def window_builder(self):
        # Barra de herramientas y botones.
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.btn_toolbar("Cargar", self.load, toolbar)
        self.btn_toolbar("Guardar", self.save, toolbar)
        self.btn_toolbar("editar", self.change_mode, toolbar)
        self.btn_toolbar("Analizar", self.analyze, toolbar)
        self.btn_toolbar("Ejecutar", self.run, toolbar)

    # Creador de botones
    def btn_toolbar(self, name: str, connect, toolbar: QToolBar):
        new_btn = QAction(name, self)
        new_btn.triggered.connect(connect)
        toolbar.addAction(new_btn)

    # Botones
    def load(self):
        pass

    def save(self):
        pass

    def change_mode(self):
        pass

    def analyze(self):
        pass

    def run(self):
        pass
