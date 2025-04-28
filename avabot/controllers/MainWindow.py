from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
from PyQt6.QtCore import pyqtSignal, QMetaObject, QThread

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton(
            "Iniciar sistema de cadastro automatizado AVA")
        self.button.clicked.connect(self.button_clicked)
        self.setCentralWidget(self.button)

        # Flag para garantir uma única instância do bot
        self.bot_thread = None

    def button_clicked(self):
        # Verifica se já existe uma thread rodando
        if self.bot_thread:
            print("Bot já está em execução. Finalizando...")
            self.bot_thread.stop()  # Encerra a thread existente
            self.bot_thread = None  # Reseta a instância

            self.button.setText("Iniciar sistema de cadastro automatizado AVA")
        else:
            # Inicia uma nova instância da thread
            self.bot_thread = BotThread()
            self.bot_thread.start()
            self.button.setText("Encerrar operação de cadastro AVA")