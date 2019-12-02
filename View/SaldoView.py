# Definição do View  para a Pessoa
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar

# ================================ PARTE DE DEMONSTRAÇÃO DO SALDO ======================================


class SaldoView:
    ''' Mostrar as informações da pessoa'''

    def __init__(self, master, controller):

        # Configuração da janela principal
        '''master=Janela Principal controller: define as ações'''
        self.controller = controller
        self.frame = tk.Frame(master)
        self.frame.pack()


        # Criação dos rótulos e os campos de texto
        self.lsaldo = tk.Label(self.frame, text = p.saldo)
    

        self.btnRecarga = tk.Button(self.frame, text="Recarga")
        self.btnMenu = tk.Button(self.frame, text="Voltar ao Menu")

        # Adicionar os widgets
        self.lsaldo.grid(row=0, column=0)
        self.esaldo.grid(row=0, column=1)
        self.btnRecarga.grid(row=1, column=0)
        self.btnMenu.grid(row=1, column=1)

        # Ações para os botões
        # Note que a ação do botão chama um método do controlador
        self.btnRecarga.bind("<Button>", lambda e: controller.entrar_recarga())

        self.btnMenu.bind("<Button>", lambda e: controller.entrar_recarga())


    def adicionar_erro(self):
        ''' Mostrar uma mensagem de erro'''
        messagebox.showerror(
            "Recarga", "Você não possui um cartão cadastrado.")

