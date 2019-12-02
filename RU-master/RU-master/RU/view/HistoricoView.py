# Definição do View  para o histórico
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar

# ================================ PARTE DE DEMONSTRAÇÃO DO HISTÓRICO ======================================


class HistoricoView:
    ''' Mostrar as informações da pessoa'''

    def __init__(self, master, controller):

        # Configuração da janela principal
        '''master=Janela Principal controller: define as ações'''
        self.controller = controller
        self.frame = tk.Frame(master)
        self.frame.pack()


        # Criação dos rótulos e os campos de texto
        self.lhistorico = tk.Label(self.frame, text=p.historico)
        
        self.btnMenu = tk.Button(self.frame, text="Voltar ao menu")


        # Adicionar os widgets
        self.lhistorico.grid(row=0, column=0)

        self.btnClean.grid(row=1, column=3)

        # Ações para os botões
        # Note que a ação do botão chama um método do controlador para retornar ao menu
        self.btnBack.bind("<Button>", lambda e: controller.retornar_menu())
