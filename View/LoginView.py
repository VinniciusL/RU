# Definição do View  para a Pessoa
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar

# ================================ PARTE DE DEMONSTRAÇÃO DO USUARIO ======================================


class LoginView:
    ''' Mostrar as informações da pessoa'''

    def __init__(self, master, controller):
        '''master=Janela Principal
           controller: define as ações
        '''
        self.controller = controller
        self.frame = tk.Frame(master)
        self.frame.pack()

        # Variaveis para os campos de texto
        self.vlogin = StringVar()
        self.vsenha = StringVar()

        # Criação dos rótulos e os campos de texto
        self.llogin = tk.Label(self.frame, text="Login:")
        self.elogin = tk.Entry(self.frame, textvariable=self.vlogin)
        self.lsenha = tk.Label(self.frame, text="Senha:")
        self.esenha = tk.Entry(self.frame, textvariable=self.vsenha)

        self.btnLogin = tk.Button(self.frame, text="Entrar")
        self.btnSignUp = tk.Button(self.frame, text="Cadastro")


        # Adicionar os widgets
        self.llogin.grid(row=0, column=0)
        self.elogin.grid(row=0, column=1)
        self.lsenha.grid(row=1, column=0)
        self.esenha.grid(row=1, column=1)

        self.btnLogin.grid(row=2, column=0)
        self.btnSignUp.grid(row=2, column=1)


        # Ações para os botões
        # Note que a ação do botão chama um método do controlador
        self.btnLogin.bind("<Button>", lambda e: controller.fazer_login(self.vlogin.get(), self.vsenha.get()))

        self.btnSignUp.bind("<Button>", lambda e: controller.cadastrar_pessoa())

    def limpar(self):
        '''Remover os textos dos campos'''
        self.vlogin.set("")
        self.vsenha.set("")

    def login_ok(self):
        '''Mostrar uma mensagem informando que a operação foi bem sucedida'''
        messagebox.showinfo("Login", "Seu login foi bem sucedido!".format(self.vcpf.get()))

    def login_erro(self):
        ''' Mostrar uma mensagem de erro'''
        messagebox.showerror("Login", "Login e/ou senha não estão corretos.".format(self.vcpf.get()))
