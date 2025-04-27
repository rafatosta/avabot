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

            # Aguarda a mudança da URL que indica que o login foi concluído
            WebDriverWait(self.driver, timeout=99999).until(
                lambda driver: driver.current_url == self.cursos)

            print("Login realizado com sucesso!")

            # Aguarda o botão com o valor 'Inscrever usuários'
            button = WebDriverWait(self.driver, timeout=99999).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="enrolusersbutton-1"]/div/input[1]'))
            )
            button.click()

            print("Botão 'Inscrever usuários' clicado com sucesso!")

            # Seleciona o botão para pesquisar alunos
            input_field = self.find_element(
                By.XPATH, '//input[@data-fieldtype="autocomplete"]', 99999)

            input_field.send_keys("Nome do aluno")
            input_field.click()

        except Exception as e:
            print(f"❌ Erro ao tentar logar: {e}")
            # self.close()
