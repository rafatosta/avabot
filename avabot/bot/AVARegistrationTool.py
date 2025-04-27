from avabot.webdrive.AvaWebDrive import AvaWebDrive
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AVARegistrationTool(AvaWebDrive):

    home = "https://ava.ifba.edu.br/my/courses.php"
    cursos = "https://ava.ifba.edu.br/my/courses.php"

    def __init__(self, headless=False, alunos: list = []):
        """Inicializa o WebDriver."""
        super().__init__(headless=headless, url=self.home)

        # Lista de alunos
        self.alunos = alunos

    def login_manual(self):
        self.driver.get(self.url)

    def exec(self):

        try:
            self.login()
            # Selecione o curso

            # 🔹 Aguarda um elemento que indica que o login foi concluído
            WebDriverWait(self.driver, timeout=99999).until(
                lambda driver: driver.current_url == self.cursos)

            print("Login realizado com sucesso!")


        except Exception as e:
            print(f"❌ Erro ao tentar logar: {e}")
            #self.close()
