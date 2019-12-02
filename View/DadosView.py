# Definição do View  para a Pessoa
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar

# ============================ PARTE DE DEMONSTRAÇÃO DO DADOS DO USUÁRIO ================================


class DadosView:
    ''' Mostrar as informações da pessoa'''

    def __init__(self, master, controller):

        # Configuração da janela principal
        '''master=Janela Principal controller: define as ações'''
        self.controller = controller
        self.frame = tk.Frame(master)
        self.frame.pack()

        # Criação dos rótulos e os campos de texto
        self.lnome = tk.Label(self.frame, text=pegar.nome)
        self.enome = tk.Entry(self.frame, textvariable=self.vnome)
        self.lcpf = tk.Label(self.frame, text=pegar.cpf)
        self.ecpf = tk.Entry(self.frame, textvariable=self.vcpf)
        self.lemail = tk.Label(self.frame, text=pegar.email)
        self.eemail = tk.Entry(self.frame, textvariable=self.vemail)
        self.lcodigoCartao = tk.Label(self.frame, text=pegar.codigoCartao)
        self.ecodigoCartao = tk.Entry(self.frame, textvariable=self.vcodigoCartao)

        self.btnBack = tk.Button(self.frame, text="Retornar ao Menu")

        # Adicionar os widgets
        self.lnome.grid(row=0, column=0)
        self.enome.grid(row=0, column=1)
        self.lcpf.grid(row=1, column=0)
        self.ecpf.grid(row=1, column=1)
        self.lemail.grid(row=2, column=0)
        self.eemail.grid(row=2, column=1)
        self.lcodigoCartao.grid(row=3, column=0)
        self.ecodigoCartao.grid(row=3, column=1)

        self.btnBack.grid(row=4, column=0)


        # Ações para os botões
        # Note que a ação do botão chama um método do controlador
        self.btnBack.bind("<Button>", lambda e: controller.retornar_menu())



