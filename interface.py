from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, 
                             QVBoxLayout, QWidget, QListWidget, 
                             QLineEdit, QLabel, QDialog, QHBoxLayout, QTextEdit)
from PyQt5.QtCore import Qt
import sys
from database.db_operations import adicionar_estudo, adicionar_passo, listar_estudos, listar_passos

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
        layout.addWidget(btn_ver)
        layout.addWidget(btn_adicionar)

        btn_ver.clicked.connect(self.abrir_passos)
        btn_adicionar.clicked.connect(self.adicionar_estudo)

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
        dialog.setGeometry(150, 150, 300, 100)

        dialog_layout = QVBoxLayout()

        label = QLabel('Título:')
        dialog_layout.addWidget(label)

        self.input_titulo = QLineEdit()
        dialog_layout.addWidget(self.input_titulo)

        btn_salvar = QPushButton('Salvar')
        dialog_layout.addWidget(btn_salvar)

        btn_salvar.clicked.connect(self.salvar_estudo)

        dialog.setLayout(dialog_layout)
        dialog.exec_()

    def salvar_estudo(self):
        titulo = self.input_titulo.text()
        if titulo:
            adicionar_estudo(titulo)
            self.carregar_estudos()
            self.sender().parent().close()

class PassosWindow(QMainWindow):
    def __init__(self, titulo_estudo):
        super().__init__()
        self.setWindowTitle(f'Estudo de Caso: {titulo_estudo}')
        self.setGeometry(200, 200, 500, 400)
        self.titulo_estudo = titulo_estudo

        # Layout principal
        layout = QVBoxLayout()

        # Exibição dos passos
        self.lista_passos = QListWidget()
        self.carregar_passos()
        layout.addWidget(QLabel('Passos:'))
        layout.addWidget(self.lista_passos)

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
        for passo in passos:
            self.lista_passos.addItem(f"Passo: {passo['passo']}\nProblema: {passo['problema']}")

    def adicionar_passo(self):
        passo_texto = self.input_passo.toPlainText()
        problema_texto = self.input_problema.toPlainText()
        if passo_texto:
            adicionar_passo(self.titulo_estudo, passo_texto, problema_texto)
            self.carregar_passos()
            self.input_passo.clear()
            self.input_problema.clear()
