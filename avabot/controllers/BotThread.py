
from PyQt6.QtCore import pyqtSignal, QThread
from avabot.bot.AVARegistrationTool import AVARegistrationTool
from avabot.services.PlanilhaHandler import PlanilhaHandler


class BotThread(QThread):

    login_success_signal = pyqtSignal()

    def __init__(self, alunos: list = []):
        super().__init__()
        self._running = True  # Flag para controlar se a thread está rodando
        self.bot = AVARegistrationTool(alunos=alunos)  # Inicializa o bot aqui

    def run(self):
        # Executa o bot em segundo plano
        try:
            self.bot.exec()
        except Exception as e:
            print(f"Erro na execução do bot: {e}")

    def stop(self):
        # Função para parar a thread (caso precise de lógica específica)
        self._running = False
        self.bot.close()
        self.quit()
        self.wait()  # Aguarda a thread terminar
