import sys
from PyQt6.QtWidgets import QApplication

from avabot.controllers.MainWindow import MainWindow


def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()



"""
Melhorias: 
- Cadastro por email: Coletar o email do Aluno no SUAP.
- Opção de gerar arquivos com emails dos alunos.
- Escolher arquivos via interface
- Lista de Alunos após escolha do arquivo

"""