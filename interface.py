import tkinter as tk
from tkinter import messagebox
from database.db_operations import adicionar_estudo

class EstudoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Gestão de Estudos de Caso')

        self.titulo_label = tk.Label(root, text='Título do Estudo de Caso:')
        self.titulo_label.pack()

        self.titulo_entry = tk.Entry(root)
        self.titulo_entry.pack()

        self.adicionar_button = tk.Button(root, text='Adicionar Estudo', command=self.adicionar_estudo)
        self.adicionar_button.pack()

    def adicionar_estudo(self):
        titulo = self.titulo_entry.get()
        if titulo:
            adicionar_estudo(titulo)
            messagebox.showinfo('Sucesso', 'Estudo de caso adicionado!')
        else:
            messagebox.showerror('Erro', 'Por favor, insira um título.')
