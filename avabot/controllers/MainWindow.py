from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QLabel, QFileDialog, QListWidget, QTextEdit
from avabot.controllers.BotThread import BotThread
from avabot.services.PlanilhaHandler import PlanilhaHandler


class MainWindow(QMainWindow):

    alunos = []

    def __init__(self):
        super().__init__()

        self.setWindowTitle("AvaBot")

        # Layout principal
        layout = QVBoxLayout()

        # Adicionando um QLabel
        self.label = QLabel("Selecione o arquivo:")
        layout.addWidget(self.label)

        # Campo de texto não editável para mostrar o caminho do arquivo
        self.file_path_edit = QLineEdit()
        self.file_path_edit.setPlaceholderText("Caminho do arquivo")
        self.file_path_edit.setReadOnly(True)  # Torna o campo não editável
        layout.addWidget(self.file_path_edit)

        # Botão para abrir o dialog de seleção de arquivo
        self.select_button = QPushButton("Selecionar Arquivo")
        self.select_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_button)

        # Lista de alunos
        self.alunos_list = QListWidget()
        layout.addWidget(self.alunos_list)

        # Área de texto para erros ou mensagens adicionais
        self.info_text = QTextEdit()
        self.info_text.setReadOnly(True)
        layout.addWidget(self.info_text)

        # Botão principal
        self.button = QPushButton(
            "Iniciar sistema de cadastro automatizado AVA")
        self.button.setDisabled(True)  # Inicialmente desabilitado
        self.button.clicked.connect(self.button_clicked)
        layout.addWidget(self.button)

        # Widget principal
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

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
            self.bot_thread = BotThread(self.alunos)
            self.bot_thread.start()
            self.button.setText("Encerrar operação de cadastro AVA")

    def select_file(self):
        # Abre o diálogo para selecionar um arquivo
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Selecionar Arquivo", "", "Todos os Arquivos (*)")

        if file_path:
            # Exibe o caminho do arquivo selecionado no campo de texto
            self.file_path_edit.setText(file_path)
            self.get_alunos()

    def get_alunos(self):
        # Limpa a lista de alunos e informações anteriores
        self.alunos_list.clear()
        self.info_text.clear()

        try:
            # Inicializa o handler para ler a planilha
            handler = PlanilhaHandler(self.file_path_edit.text())
            dados_planilha = handler.ler_planilha()

            self.alunos = []

            for linha in dados_planilha:
                # Adiciona o nome do aluno à lista
                self.alunos.append(linha.get('Nome'))

            # Atualiza a lista de alunos na interface
            for aluno in self.alunos:
                self.alunos_list.addItem(aluno)

            # Mostra a quantidade de alunos na área de texto
            self.info_text.append(f"📊 Total de alunos: {len(self.alunos)}")

            # Habilita o botão, pois a lista foi carregada sem erros
            self.button.setEnabled(True)

        except Exception as e:
            # Captura erros ao tentar abrir ou ler o arquivo
            self.info_text.append(f"❌ Erro ao abrir o arquivo: {str(e)}")
            self.button.setDisabled(True)  # Desabilita o botão se ocorrer erro
