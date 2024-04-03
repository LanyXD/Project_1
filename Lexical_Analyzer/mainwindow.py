from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QToolBar, QFileDialog, QVBoxLayout, QWidget, QTextEdit, QLabel
from string_parser import StringParcer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 500)
        self.setWindowTitle("Analizador")
        self.text2 = []

        # Variables para el text edit
        self.textedit = QTextEdit()
        self.textedit.setEnabled(False)

        # Variables para el label
        self.label = QLabel()

        # Variables para el layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.textedit)
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
        button_action2.triggered.connect(self.analizar)
        toolbar.addAction(button_action2)

    def load(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialog_succesful = dialog.exec()
        if dialog_succesful:
            file_location = dialog.selectedFiles()[0]
            with open(file_location, 'rb') as file:
                text = str(file.read()).split(sep="'")[1]
                self.text2 = text.split(sep='\\r\\n')
                text3 = ''
                for i in self.text2:
                    text3 += i
                    text3 += "\n"

                self.textedit.setText(text3)
                file.close()

    def analizar(self):
        flag = False
        text2 = "Cadena no aceptada."
        analizador = StringParcer()
        for i in self.text2:
            analizador.set_string(i)
            try:
                analizador.analyze_text()

            except:
                flag = True
        results = analizador.resultados()
        text = (f'Palabras reservadas: {results[0]} \n Operadores: {results[1]} \n Signos: {results[2]}'
                f'\n Numeros: {results[3]} \n Identificadores: {results[4]}')
        if flag is True:
            self.label.setText(text2)
        else:
            self.label.setText(text)
