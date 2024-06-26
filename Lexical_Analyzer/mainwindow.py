from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QToolBar, QFileDialog, QVBoxLayout, QWidget, QLabel, QMessageBox
from string_parser import StringParcer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 500)
        self.setWindowTitle("Analizador")
        self.fileText: list = []
        self.labelList: list = []
        self.badStrings: list = []

        # Variables para el layout
        self.main_layout = QVBoxLayout()

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

    def clean_screen(self):
        for i in self.labelList:
            self.main_layout.removeWidget(i)

        self.fileText.clear()
        self.labelList.clear()
        self.badStrings.clear()

    def load(self):
        self.clean_screen()

        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialog_succesful = dialog.exec()
        if dialog_succesful:
            file_location = dialog.selectedFiles()[0]
            with open(file_location, 'rb') as file:
                text = str(file.read()).split(sep="'")[1]
                self.fileText = text.split(sep='\\r\\n')
                self.load_text()
                file.close()

    def load_text(self):
        for text in self.fileText:
            new_label = QLabel()
            new_label.setText(text)
            new_label.setMinimumSize(10, 10)
            new_label.setMaximumSize(1100, 20)

            self.labelList.append(new_label)
            self.main_layout.addWidget(new_label)

    def analizar(self):
        flag = False
        count = 0

        analizador = StringParcer()
        for i in self.fileText:
            analizador.set_string(i)
            label: QLabel = self.labelList[count]
            try:
                analizador.analyze_text()
            except:
                label.setStyleSheet('background-color: red')
                self.badStrings.append(count + 1)
                flag = True
            else:
                label.setStyleSheet('background-color: green')

            count += 1

        results = analizador.resultados()
        text = (f'Palabras reservadas: {results[0]} \n Operadores: {results[1]} \n Signos: {results[2]}'
                f'\n Numeros: {results[3]} \n Identificadores: {results[4]}')

        if flag is True:
            self.bad_message()
        else:
            self.good_message(text)

    def good_message(self, result):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("RESULTADO")
        dlg.setText(result)
        dlg.show()

    def bad_message(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("CADENAS INCORRECTAS")
        text = ''

        for i in self.badStrings:
            text += f"Error en la linea: {i}\n"

        dlg.setText(text)
        dlg.show()
