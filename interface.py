from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, 
                             QVBoxLayout, QWidget, QListWidget, 
                             QLineEdit, QLabel, QDialog, QHBoxLayout, QTextEdit, QMessageBox)
from PyQt5.QtCore import Qt
import sys
from database.db_operations import adicionar_estudo, adicionar_passo, listar_estudos, listar_passos, obter_estudo_id_por_titulo, excluir_passo, excluir_todos_passos, excluir_estudo

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Gestão de Estudos de Caso')
        self.setGeometry(100, 100, 600, 400)

        # Layout principal
        layout = QVBoxLayout()

        # Lista de estudos de caso
        self.lista_estudos = QListWidget()
        self.carregar_estudos()
        layout.addWidget(QLabel('Estudos de Caso:'))
        layout.addWidget(self.lista_estudos)

        # Botões
        btn_ver = QPushButton('Ver Estudo')
        btn_adicionar = QPushButton('Adicionar Estudo')
        btn_excluir_estudo = QPushButton('Excluir Estudo Selecionado')
        layout.addWidget(btn_ver)
        layout.addWidget(btn_adicionar)
        layout.addWidget(btn_excluir_estudo)

        btn_ver.clicked.connect(self.abrir_passos)
        btn_adicionar.clicked.connect(self.adicionar_estudo)
        btn_excluir_estudo.clicked.connect(self.excluir_estudo_selecionado)

        # Configuração do layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def carregar_estudos(self):
        self.lista_estudos.clear()
        estudos = listar_estudos()
        for estudo in estudos:
            self.lista_estudos.addItem(estudo['titulo'])

    def abrir_passos(self):
        item = self.lista_estudos.currentItem()
        if item:
            titulo = item.text()
            self.passos_window = PassosWindow(titulo)
            self.passos_window.show()

    def adicionar_estudo(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Adicionar Estudo de Caso')
        dialog.setGeometry(150, 150, 400, 200)

        dialog_layout = QVBoxLayout()

        # Campo para título
        label_titulo = QLabel('Título:')
        dialog_layout.addWidget(label_titulo)
        self.input_titulo = QLineEdit()
        dialog_layout.addWidget(self.input_titulo)

        # Campo para o primeiro passo
        label_passo = QLabel('Primeiro Passo:')
        dialog_layout.addWidget(label_passo)
        self.input_passo = QTextEdit()
        dialog_layout.addWidget(self.input_passo)

        # Campo para problema (opcional)
        label_problema = QLabel('Problema (opcional):')
        dialog_layout.addWidget(label_problema)
        self.input_problema = QTextEdit()
        dialog_layout.addWidget(self.input_problema)

        btn_salvar = QPushButton('Salvar')
        dialog_layout.addWidget(btn_salvar)

        btn_salvar.clicked.connect(self.salvar_estudo)

        dialog.setLayout(dialog_layout)
        dialog.exec_()

    def salvar_estudo(self):
        titulo = self.input_titulo.text()
        passo = self.input_passo.toPlainText()
        problema = self.input_problema.toPlainText()

        if titulo:
            adicionar_estudo(titulo)
            estudo_id = obter_estudo_id_por_titulo(titulo)
            if passo:
                adicionar_passo(estudo_id, passo, problema)
            self.carregar_estudos()
            self.sender().parent().close()

    def excluir_estudo_selecionado(self):
        item = self.lista_estudos.currentItem()
        if item:
            titulo = item.text()
            estudo_id = obter_estudo_id_por_titulo(titulo)
            resposta = QMessageBox.question(self, 'Confirmação', f'Tem certeza que deseja excluir o estudo "{titulo}" e todos os passos associados?', QMessageBox.Yes | QMessageBox.No)
            if resposta == QMessageBox.Yes:
                excluir_estudo(estudo_id)
                self.carregar_estudos()
        else:
            QMessageBox.warning(self, 'Atenção', 'Selecione um estudo de caso para excluir.')

class PassosWindow(QMainWindow):
    def __init__(self, titulo_estudo):
        super().__init__()
        self.setWindowTitle(f'Estudo de Caso: {titulo_estudo}')
        self.setGeometry(200, 200, 500, 500)
        self.titulo_estudo = titulo_estudo

        # Layout principal
        layout = QVBoxLayout()

        # Exibição dos passos
        self.lista_passos = QListWidget()
        self.carregar_passos()
        layout.addWidget(QLabel('Passos:'))
        layout.addWidget(self.lista_passos)

        # Botões de exclusão
        btn_excluir_passo = QPushButton('Excluir Passo Selecionado')
        btn_excluir_todos = QPushButton('Excluir Todos os Passos')
        layout.addWidget(btn_excluir_passo)
        layout.addWidget(btn_excluir_todos)

        btn_excluir_passo.clicked.connect(self.excluir_passo_selecionado)
        btn_excluir_todos.clicked.connect(self.excluir_todos_passos)

        # Área para adicionar novos passos
        self.input_passo = QTextEdit()
        layout.addWidget(QLabel('Novo Passo:'))
        layout.addWidget(self.input_passo)

        self.input_problema = QTextEdit()
        layout.addWidget(QLabel('Problema (opcional):'))
        layout.addWidget(self.input_problema)

        btn_adicionar_passo = QPushButton('Adicionar Passo')
        layout.addWidget(btn_adicionar_passo)

        btn_adicionar_passo.clicked.connect(self.adicionar_passo)

        # Configuração do layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def carregar_passos(self):
        self.lista_passos.clear()
        passos = listar_passos(self.titulo_estudo)
        for i, passo in enumerate(passos):
            self.lista_passos.addItem(f"Passo {i+1}: {passo['passo']}\nProblema: {passo['problema']}")

    def adicionar_passo(self):
        passo_texto = self.input_passo.toPlainText()
        problema_texto = self.input_problema.toPlainText()
        if passo_texto:
            estudo_id = obter_estudo_id_por_titulo(self.titulo_estudo)
            adicionar_passo(estudo_id, passo_texto, problema_texto)
            self.carregar_passos()
            self.input_passo.clear()
            self.input_problema.clear()

    def excluir_passo_selecionado(self):
        item_selecionado = self.lista_passos.currentRow()
        if item_selecionado >= 0:
            estudo_id = obter_estudo_id_por_titulo(self.titulo_estudo)
            passos = listar_passos(self.titulo_estudo)
            passo_id = passos[item_selecionado]['id']
            resposta = QMessageBox.question(self, 'Confirmação', 'Tem certeza que deseja excluir o passo selecionado?', QMessageBox.Yes | QMessageBox.No)
            if resposta == QMessageBox.Yes:
                excluir_passo(passo_id)
                self.carregar_passos()
        else:
            QMessageBox.warning(self, 'Atenção', 'Selecione um passo para excluir.')

    def excluir_todos_passos(self):
        estudo_id = obter_estudo_id_por_titulo(self.titulo_estudo)
        resposta = QMessageBox.question(self, 'Confirmação', 'Tem certeza que deseja excluir todos os passos?', QMessageBox.Yes | QMessageBox.No)
        if resposta == QMessageBox.Yes:
            excluir_todos_passos(estudo_id)
            self.carregar_passos()
