# Definição do View  para a Pessoa
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar

# ================================ PARTE DE DEMONSTRAÇÃO DO CARTÃO ======================================


class CadastroView:
    ''' Mostrar as informações da pessoa'''

    def __init__(self, master, controller):

        # Configuração da janela principal
        '''master=Janela Principal controller: define as ações'''
        self.controller = controller
        self.frame = tk.Frame(master)
        self.frame.pack()

        # Variaveis para os campos de texto
        self.vnome = StringVar()
        self.vcpf = StringVar()
        self.vlogin = StringVar()
        self.vsenha = StringVar()

        # Criação dos rótulos e os campos de texto
        self.lnome = tk.Label(self.frame, text="Nome:")
        self.enome = tk.Entry(self.frame, textvariable=self.vnome)
        self.lcpf = tk.Label(self.frame, text="CPF:")
        self.ecpf = tk.Entry(self.frame, textvariable=self.vcpf)
        self.llogin = tk.Label(self.frame, text="Saldo:")
        self.elogin = tk.Entry(self.frame, textvariable=self.vlogin)
        self.lsenha = tk.Label(self.frame, text="Usuario:")
        self.esenha = tk.Entry(self.frame, textvariable=self.vsenha)
        
        self.btnReturn = tk.Button(self.frame, text="Retornar ao Login")
        self.btnSignIn = tk.Button(self.frame, text="Cadastrar")

        # Adicionar os widgets
        self.lnome.grid(row=0, column=0)
        self.enome.grid(row=0, column=1)
        self.lcpf.grid(row=1, column=0)
        self.ecpf.grid(row=1, column=1)
        self.llogin.grid(row=2, column=0)
        self.elogin.grid(row=2, column=1)
        self.lsenha.grid(row=3, column=0)
        self.esenha.grid(row=3, column=1)
        
        self.btnReturn.grid(row=4, column=0)
        self.btnSignIn.grid(row=4, column=1)

        # Ações para os botões
        # Note que a ação do botão chama um método do controlador
        self.btnReturn.bind("<Button>", lambda e: controller.retornar_menu())

        self.btnSignIn.bind("<Button>", lambda e: controller.cadastro_usuario())
