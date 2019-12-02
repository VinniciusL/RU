# Definição do View  para a Pessoa
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar

# ================================ PARTE DE DEMONSTRAÇÃO DO MENU ======================================


class MenuView:
    ''' Mostrar as informações da pessoa'''

    def __init__(self, master, controller):
        '''master=Janela Principal
           controller: define as ações
        '''
        self.controller = controller
        self.frame = tk.Frame(master)
        self.frame.pack()

        # Criação dos rótulos e os campos de texto

        self.btnDados = tk.Button(self.frame, text="Dados do Usuário")
        self.btnRecarga = tk.Button(self.frame, text="Recarga do Cartão")
        self.btnSaldo = tk.Button(self.frame, text="Verificar Saldo")
        self.btnMenu = tk.Button(self.frame, text="Escolher Menu")
        self.btnHistorico = tk.Button(self.frame, text="Histórico de Compras")

        # Adicionar os widgets
        self.btnDados.grid(row=0, column=0)
        self.btnRecarga.grid(row=1, column=0)
        self.btnSaldo.grid(row=2, column=0)
        self.btnMenu.grid(row=3, column=0)
        self.btnHistorico.grid(row=4, column=0)

        # Ações para os botões
        # Note que a ação do botão chama um método do controlador
        self.btnDados.bind("<Button>", lambda e: controller.entrar_dados())

        self.btnRecarga.bind("<Button>", lambda e: controller.entrar_recarga())

        # A ação deste botão chama direitamente um dos métodos do view
        self.btnSaldo.bind("<Button>", lambda e: self.entrar_saldo())

        # A ação deste botão é para ir diretamente a parte dos cartões
        self.btnMenu.bind("<Button>", lambda e: self.entrar_menu())
        
        # A ação deste botão é para ir diretamente a parte dos cartões
        self.btnHistorico.bind("<Button>", lambda e: self.entrar_historico())


    def recarga_cartao_erro(self):
        '''Mostrar uma mensagem informando que ocorreu um erro'''
        messagebox.showerror("Cartão", "Você não possui um cartão cadastrado para fazer recarga.")
        
    def verificar_cartao_erro(self):
        '''Mostrar uma mensagem informando que ocorreu um erro'''
    messagebox.showerror("Cartão", "Você não possui um cartão cadastrado para verificar o saldo.")



