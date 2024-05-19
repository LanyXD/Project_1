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
from PyQt6.QtGui import QAction, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # variables y banderas
        self.text: str = ""
        self.mode: bool = False
        self.flag: bool = True

        # layouts
        self.main_layout: QVBoxLayout = QVBoxLayout()
        self.stack_layout: QStackedLayout = QStackedLayout()
        self.console_layout: QTextEdit = QTextEdit()

        # layouts en stack_layout
        self.edit_layout: QTextEdit = QTextEdit()
        self.v_layout: QVBoxLayout = QVBoxLayout()

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
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setEnabled(True)

        # v_layout
        scroll.setLayout(self.v_layout)

        # Stack Layout
        self.stack_layout.addWidget(scroll)
        self.stack_layout.addWidget(self.edit_layout)

        # consola
        self.console_layout.setEnabled(False)
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

    # Creador de botones
    def btn_toolbar(self, name: str, function, toolbar: QToolBar):
        new_btn = QAction(name, self)
        new_btn.triggered.connect(function)
        toolbar.addAction(new_btn)
        return new_btn

    # Botones
    def load(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialog_successful = dialog.exec()

        if dialog_successful:
            file_location = dialog.selectedFiles()[0]
            with open(file_location, 'rb') as file:
                self.text = str(file.read(), "UTF-8")
                file.close()

        self.load_text()

    def save(self):
        new_text = self.edit_layout.toPlainText()
        self.text = new_text

        self.load_text()

    def console(self):
        if self.flag:
            self.flag = False
            self.console_layout.close()
        else:
            self.flag = True
            self.console_layout.show()

    def change_mode(self):
        if self.mode:
            self.stack_layout.setCurrentIndex(0)
            self.mode = False
        else:
            self.stack_layout.setCurrentIndex(1)
            self.mode = True

    def analyze(self):
        pass

    def run(self):
        pass

    # otras funciones
    def load_text(self):
        for text in self.text.split("\n"):
            new_widget = QLabel(text)
            self.v_layout.addWidget(new_widget)

        self.edit_layout.setText(self.text)
