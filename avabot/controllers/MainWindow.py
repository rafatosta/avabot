from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog, QListWidget, QSizePolicy
from avabot.controllers.BotThread import BotThread
from avabot.services.Parser import Parser
from avabot.services.PlanilhaHandler import PlanilhaHandler


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Definindo o título da janela
        self.setWindowTitle("Cadastro Automatizado AVA")
        self.setGeometry(100, 100, 800, 600)

        # Layout principal
        layout = QVBoxLayout()

        # Label para indicar o arquivo
        self.label = QLabel("Selecione o arquivo contendo os alunos:")
        layout.addWidget(self.label)

        # Campo de texto não editável para exibir o caminho do arquivo
        self.lineEdit = QLineEdit()
        self.lineEdit.setReadOnly(True)  # Torna o campo não editável
        layout.addWidget(self.lineEdit)

        # Botão para selecionar o arquivo
        self.selectButton = QPushButton("Selecionar Arquivo")
        self.selectButton.clicked.connect(self.select_file)
        layout.addWidget(self.selectButton)

        # Lista para mostrar os alunos
        self.listWidget = QListWidget()
        self.listWidget.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding) 
        layout.addWidget(self.listWidget)

        # Campo de texto para mostrar informações de erro ou sucesso
        self.infoText = QLabel()
        layout.addWidget(self.infoText)

        # Botão para iniciar o sistema de cadastro
        self.pushButton = QPushButton(
            "Iniciar sistema de cadastro automatizado AVA")
        self.pushButton.setDisabled(True)  # Inicialmente desabilitado
        self.pushButton.clicked.connect(self.button_clicked)
        layout.addWidget(self.pushButton)

        # Widget principal
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Inicializando as variáveis
        self.bot_thread = None
        self.alunos = []

    def select_file(self):
        # Abre o diálogo para selecionar um arquivo
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Selecionar Arquivo", "", "Todos os Arquivos (*)")
        if file_path:
            # Exibe o caminho do arquivo no campo de texto
            self.lineEdit.setText(file_path)
            self.get_alunos(file_path)

    def get_alunos(self, file_path):
        # Limpa a lista de alunos e as informações anteriores
        self.listWidget.clear()
        self.infoText.clear()
        self.alunos = []

        try:
            # Inicializa o handler para ler a planilha
            handler = PlanilhaHandler(file_path)
            dados_planilha = handler.ler_planilha()

            # Adiciona os alunos na lista
            for linha in dados_planilha:

                nome = linha.get('Nome')
                nome_secundario = Parser.extrair_nome_secundario(nome)

                self.alunos.append(nome_secundario)

            # Atualiza a lista de alunos na interface
            for aluno in self.alunos:
                self.listWidget.addItem(aluno)

            # Exibe a quantidade de alunos e habilita o botão
            self.infoText.setText(f"📊 Total de alunos: {len(self.alunos)}")
            self.pushButton.setEnabled(True)

        except Exception as e:
            # Captura erros ao tentar abrir ou ler o arquivo
            self.infoText.setText(f"❌ Erro ao abrir o arquivo: {str(e)}")
            # Desabilita o botão em caso de erro
            self.pushButton.setDisabled(True)

    def button_clicked(self):
        # Verifica se já existe uma thread rodando
        if self.bot_thread:
            print("Bot já está em execução. Finalizando...")
            self.bot_thread.stop()  # Encerra a thread existente
            self.bot_thread = None  # Reseta a instância
            self.pushButton.setText(
                "Iniciar sistema de cadastro automatizado AVA")
        else:
            # Inicia uma nova instância da thread
            self.bot_thread = BotThread(self.alunos)
            self.bot_thread.start()
            self.pushButton.setText("Encerrar operação de cadastro AVA")
