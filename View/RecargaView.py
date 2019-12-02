# Definição do View  para a Pessoa
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar

# ================================ PARTE DE DEMONSTRAÇÃO DA RECARGA ======================================


class RecargaView:
    ''' Mostrar as informações da pessoa'''

    def __init__(self, master, controller):

        # Configuração da janela principal
        '''master=Janela Principal controller: define as ações'''
        self.controller = controller
        self.frame = tk.Frame(master)
        self.frame.pack()

        # Variaveis para os campos de texto
        self.vrecarga = StringVar()


        # Criação dos rótulos e os campos de texto
        self.lrecarga = tk.Label(self.frame, text="Valor da Recarga em R$: ")
        self.erecarga = tk.Entry(self.frame, textvariable=self.vrecarga)

        self.btnOk = tk.Button(self.frame, text="Confirmar")
        self.btnCancelar = tk.Button(self.frame, text="Cancelar")
        self.btnMenu = tk.Button(self.frame, text="Retornar ao Menu")

        # Adicionar os widgets
        self.lrecarga.grid(row=0, column=0)
        self.erecarga.grid(row=0, column=1)

        self.btnOk.grid(row=4, column=0)
        self.btnCancelar.grid(row=4, column=1)
        self.btnMenu.grid(row=5, column=3)

        # Ações para os botões
        # Note que a ação do botão chama um método do controlador
        self.btnOk.bind("<Button>", lambda e: controller.recarga_cartao())

        self.btnCancelar.bind("<Button>", lambda e: controller.entrar_menu())

        # A ação deste botão chama direitamente um dos métodos do view
        self.btnMenu.bind("<Button>", lambda e: controller.entrar_menu())

    def recarga_ok(self):
        '''Mostrar uma mensagem informando que a operação foi bem sucedida'''
        messagebox.showinfo("Recarga", "Recarga concluida com sucesso.")

    def adicionar_erro(self):
        ''' Mostrar uma mensagem de erro'''
        messagebox.showerror("Recarga", "Impossível fazer recarga.")

    