import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
from avabot.bot.AVARegistrationTool import AVARegistrationTool
from PyQt6.QtCore import QThread

class BotThread(QThread):
    def __init__(self):
        super().__init__()
        self._running = True  # Flag para controlar se a thread está rodando

    def run(self):
        # Inicializa o AVARegistrationTool e executa
        self.bot = AVARegistrationTool()
        self.bot.exec()

    def stop(self):
        # Função para parar a thread (caso precise de lógica específica)
        self._running = False
        self.bot.close()
        self.quit()
        self.wait()  # Aguarda a thread terminar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("Iniciar sistema de cadastro automatizado AVA")
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


def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

    """
        1 - Carregar lista de alunos
        2 - Abrir o AVA e realizar login
    """

    """
        1 - Selecionar o Curso: https://ava.ifba.edu.br/my/courses.php
    """


if __name__ == "__main__":
    main()
