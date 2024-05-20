from PyQt6.QtWidgets import \
    QMainWindow, \
    QWidget, \
    QToolBar, \
    QVBoxLayout, \
    QHBoxLayout, \
    QStackedLayout, \
    QFileDialog, \
    QTextEdit, \
    QLabel, \
    QScrollArea
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from lexical_analyzer import LexicalAnalyzer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # variables y banderas
        self.text: str
        self.console_text: str = "Consola: \n"
        self.mode_flag: bool = False
        self.console_flag: bool = True

        # contenedor
        self.container = QWidget()

        # layouts
        self.main_layout: QVBoxLayout = QVBoxLayout()
        self.stack_layout: QStackedLayout = QStackedLayout()
        self.console_layout: QTextEdit = QTextEdit(self.console_text)

        # layouts en stack_layout
        self.edit_layout: QTextEdit = QTextEdit()
        self.v_layout: QVBoxLayout = QVBoxLayout(self.container)

        # inicializacion
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
        self.btn_toolbar("Consola", self.console, toolbar)
        self.btn_toolbar("Cambiar modo", self.change_mode, toolbar)
        self.btn_toolbar("Analizar", self.analyze, toolbar)
        self.btn_toolbar("Ejecutar", self.run, toolbar)

        # scroll area
        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)

        # v_layout
        scroll.setWidget(self.container)

        # Stack Layout
        self.stack_layout.addWidget(scroll)
        self.stack_layout.addWidget(self.edit_layout)

        # consola
        self.console_layout.setReadOnly(True)
        self.console_layout.setMaximumSize(780, 150)
        self.console_layout.setMinimumSize(780, 150)

        stack_widget = QWidget()
        stack_widget.setLayout(self.stack_layout)

        self.main_layout.addWidget(stack_widget)
        self.main_layout.addWidget(self.console_layout)

        # Caja central
        main_widget = QWidget()
        main_widget.setLayout(self.main_layout)
        self.setCentralWidget(main_widget)

    # Botones
    def load(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialog_successful = dialog.exec()

        if dialog_successful:
            file_location = dialog.selectedFiles()[0]
            with open(file_location, 'rb') as file:
                text = str(file.read(), "UTF-8")
                file.close()

        self.text = text
        self.load_text()

    def save(self):
        new_text = self.edit_layout.toPlainText()
        self.text = new_text

        self.load_text()

    def console(self):
        if self.console_flag:
            self.console_flag = False
            self.console_layout.close()
        else:
            self.console_flag = True
            self.console_layout.show()

    def change_mode(self):
        if self.mode_flag:
            self.stack_layout.setCurrentIndex(0)
            self.mode_flag = False
        else:
            self.stack_layout.setCurrentIndex(1)
            self.mode_flag = True

    def analyze(self):
        a1, analyzer = self._lexical_analyzer()
        self.console_layout.setText(self.console_text)

    def run(self):
        pass

    # Carga el texto a los layouts del stack.
    def load_text(self):
        self.cleaner()

        count = 0
        for text in self.text.split("\n"):
            count += 1
            new_widget = ObjectWidget(text, f"{count}")
            self.v_layout.addWidget(new_widget)

        self.edit_layout.setText(self.text)

    def cleaner(self):
        while self.v_layout.count():
            item = self.v_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    # Creador de botones
    def btn_toolbar(self, name: str, function, toolbar: QToolBar):
        new_btn = QAction(name, self)
        new_btn.triggered.connect(function)
        toolbar.addAction(new_btn)
        return new_btn

    def _lexical_analyzer(self):
        self.cleaner()

        flag = False
        count = 0
        error_text = ""
        analyzer = LexicalAnalyzer()

        for text in self.text.split("\n"):
            analyzer.set_string(text)
            count += 1
            try:
                analyzer.analyze_text()
            except:
                error_text += f"Error lexico en la linea: {count}. \n"
                error_text += f"Error: {text}"
                new_widget = ObjectWidget(text, f"{count}", color="white", back_color="red")
                flag = True
            else:
                new_widget = ObjectWidget(text, f"{count}", color="white", back_color="green")

            self.v_layout.addWidget(new_widget)

        self.console_text += error_text
        return flag, analyzer

    def _syntactic_analyzer(self):
        pass

    def _semantic_analyzer(self):
        pass


class ObjectWidget(QWidget):
    def __init__(self, text: str, count: str, color: str = "black", back_color: str = "yellow"):
        super().__init__()
        # tamaño de los widget
        self.setFixedHeight(30)

        # variables
        self.count = count
        self.text = text
        c = f"{self.count}."

        # labels
        self.text_label = QLabel(self.text)
        self.count_label = QLabel(c)

        # labels propiedades
        self.count_label.setFixedSize(20, 20)
        self.text_label.setMinimumHeight(20)

        # labels estilos
        self.count_label.setStyleSheet(
            f"""
            color: {color};
            background-color: {back_color}; 
            font-size: 14px;
            font-weight: bold;
            font-style: arial; 
            """)

        # Contenedores
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.count_label)
        self.h_layout.addWidget(self.text_label)

        self.setLayout(self.h_layout)
