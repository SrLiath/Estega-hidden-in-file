import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QWidget, QMessageBox, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor, QFont


class SteganographyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Estega - hidden in file")
        self.setGeometry(100, 100,400, 300)
        self.setStyleSheet("background-color: #2c2c2c; color: #ffffff;")

        layout = QVBoxLayout()

        #arquivos
        self.label_carrier = QLabel("Arquivo portador: Nenhum selecionado")
        self.label_carrier.setStyleSheet("padding: 5px;")
        self.label_hidden = QLabel("Arquivo a esconder: Nenhum selecionado")
        self.label_hidden.setStyleSheet("padding: 5px;")
        layout.addWidget(self.label_carrier)
        layout.addWidget(self.label_hidden)
        self.btn_select_carrier = self.create_button("Selecionar arquivo portador", self.select_carrier_file)
        self.btn_select_hidden = self.create_button("Selecionar arquivo a esconder", self.select_hidden_file)
        self.btn_embed = self.create_button("Esconder arquivo", self.embed_file)
        self.btn_extract = self.create_button("Extrair arquivos escondidos", self.extract_files)
        layout.addWidget(self.btn_select_carrier)
        layout.addWidget(self.btn_select_hidden)
        layout.addWidget(self.btn_embed)
        layout.addWidget(self.btn_extract)

        # espaço
        layout.addStretch()
        container = QWidget()
        container.setLayout(layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(container)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.carrier_file = None
        self.hidden_file = None

    def create_button(self, text, callback):
        """Cria um botão estilizado com tema escuro"""
        button = QPushButton(text)
        button.setStyleSheet("""
            QPushButton {
                background-color: #444;
                border: 1px solid #555;
                color: #fff;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #555;
            }
            QPushButton:pressed {
                background-color: #666;
            }
        """)
        button.clicked.connect(callback)
        return button

    def select_carrier_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecionar arquivo portador")
        if file_path:
            self.carrier_file = file_path
            self.label_carrier.setText(f"Arquivo portador: {file_path}")

    def select_hidden_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecionar arquivo a esconder")
        if file_path:
            self.hidden_file = file_path
            self.label_hidden.setText(f"Arquivo a esconder: {file_path}")

    def embed_file(self):
        if not self.carrier_file or not self.hidden_file:
            QMessageBox.warning(self, "Erro", "Selecione os dois arquivos antes de prosseguir.")
            return

        try:
            with open(self.carrier_file, "ab") as carrier, open(self.hidden_file, "rb") as hidden:
                carrier.write(hidden.read())
                carrier.write(b"---FIM_ARQUIVO---")
            QMessageBox.information(self, "Sucesso", "Arquivo escondido com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao esconder arquivo: {e}")

    def extract_files(self):
        if not self.carrier_file:
            QMessageBox.warning(self, "Erro", "Selecione o arquivo portador antes de prosseguir.")
            return

        try:
            with open(self.carrier_file, "rb") as carrier:
                data = carrier.read()
                parts = data.split(b"---FIM_ARQUIVO---")
                for i, part in enumerate(parts[:-1]):  # Exclui o último vazio
                    output_file = f"extraido_{i + 1}.bin"
                    with open(output_file, "wb") as out:
                        out.write(part)
            QMessageBox.information(self, "Sucesso", "Arquivos extraídos com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao extrair arquivos: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SteganographyApp()
    window.show()
    sys.exit(app.exec())
