# Definição do View  para a Pessoa
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar

# ================================ PARTE DE DEMONSTRAÇÃO DO CARDÁPIO ======================================


class CardapioView:
    ''' Mostrar as informações da pessoa'''

    def __init__(self, master, controller):

        # Configuração da janela principal
        '''master=Janela Principal controller: define as ações'''
        self.controller = controller
        self.frame = tk.Frame(master)
        self.frame.pack()

        # Criação dos rótulos e os campos de texto
        self.lrefeicao = tk.Label(self.frame, text=p.refeicao)

        self.btnCompra = tk.Button(self.frame, text="Realizar Compra")
        self.btnMenu = tk.Button(self.frame, text="Voltar ao Menu")

        # Adicionar os widgets
        self.lrefeicao.grid(row=0, column=0)
        
        self.btnCompra.grid(row=1, column=0)
        self.btnMenu.grid(row=1, column=3)

        # Ações para os botões
        self.btnCompra.bind("<Button>", lambda e: controller.efetuar_compra())
        self.btnMenu.bind("<Button>", lambda e: controller.entrar_menu())

    def adicionar_ok(self):
        '''Mostrar uma mensagem informando que a operação foi bem sucedida'''
        messagebox.showinfo("Refeição", "Refeição comprada com sucesso!")

    def adicionar_erro(self):
        ''' Mostrar uma mensagem de erro'''
        messagebox.showerror("Refeição", "Refeição não autorizada. Verifique seu saldo.")

    def mostrar_saldo(self, p, win):
        '''
        Mostrar as informações da pessoa
        Note que esta função retorna outra função (necessária para
        implementar o command do botão)
        '''
        def fmostrar(e):
            self.vsaldo.set(p.saldo)
            self.vusuario.set(p.usuario)
            # Fechar a janela
            win.destroy()
            self.esaldo.focus_set()
        return fmostrar

    def listar(self, C):
        '''Mostrar a lista de alimentos disponível no Cardápio'''
        win = tk.Toplevel()
        win.wm_title("Lista de Alimentos")

        tk.Label(win, text="Alimentos: ", bg="black", fg="white", width=5).grid(row=0, column=0)
        i = 1
        for p in C:
            Lrefeicao = tk.Label(win, text=p.refeicao, fg="blue")
            Lrefeicao.bind("<Button>", self.listar_refeicao(p, win))
            Lrefeicao.grid(row=i, column=0)
            tk.Label(win, text=p.alimento).grid(row=i, column=1)
            tk.Label(win, text=p.saldo).grid(row=i, column=2)
            i += 1