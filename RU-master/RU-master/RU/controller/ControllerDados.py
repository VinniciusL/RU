#Classe do controlador

import tkinter as tk
from DadosView import DadosView
from genericDao import GenericDao



class Controller:

    def __init__(self):
        # Criar a Janela principal
        self.root = tk.Tk()
        self.root.geometry('800x400+100+100')
        self.root.title('Dados do Usuário')

        # Criar o objeto View
        self.view = DadosView(self.root, self)

        #Loop
        self.root.mainloop()
        