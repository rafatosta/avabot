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

            for aluno in self.alunos:
                print("Adicionando aluno(a):", aluno)

                # Seleciona o botão para pesquisar alunos
                input_field = WebDriverWait(self.driver, 99999).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, '//input[@data-fieldtype="autocomplete"]'))
                )
                input_field.send_keys(aluno)

                # Aguarda até que o elemento da sugestão esteja disponível
                input_aluno = WebDriverWait(self.driver, 99999).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, '(//ul[@class="form-autocomplete-suggestions"]//li)[1]'))
                )
                input_aluno.click()

                # Limpa o nome
                input_field.clear()
        except Exception as e:
            print(f"❌ Erro ao tentar logar: {e}")
            # self.close()
