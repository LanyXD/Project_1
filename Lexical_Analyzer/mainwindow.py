from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QToolBar, QFileDialog, QLabel, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 500)
        self.setWindowTitle("Analizador")

        # Variables para los labels
        self.label = QLabel()

        # Variables para el layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.label)

        # Variables para los widgets
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

        # Variables para la barra de tareas
        toolbar = QToolBar("toolbar")
        self.addToolBar(toolbar)

        # Variables para los botones de la barra de tareas
        # Boton para cargar un archivo de texto
        button_action1 = QAction("Cargar", self)
        button_action1.setStatusTip("Cargar un archivo de texto")
        button_action1.triggered.connect(self.load)
        toolbar.addAction(button_action1)

        # Boton para analizar el archivo de texto
        button_action2 = QAction("Analizar", self)
        button_action2.setStatusTip("Analiza el archivo cargado")
        button_action1.triggered.connect(self.analizar)
        toolbar.addAction(button_action2)

    def load(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialog_succesful = dialog.exec()
        if dialog_succesful:
            file_location = dialog.selectedFiles()[0]
            with open(file_location, 'rb') as file:
                text = str(file.read()).split(sep="'")[1]
                text2 = text.split(sep='\\r\\n')
                text3 = ''
                for i in text2:
                    text3 += i
                    text3 += "\n"

                self.label.setText(text3)
                file.close()

    def analizar(self):
        pass
