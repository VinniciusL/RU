#Classe do controlador

import tkinter as tk
from CadastroView import CadastroView
from genericDao import GenericDao


class Controller:

    def __init__(self):
        # Criar a Janela principal
        self.root = tk.Tk()
        self.root.geometry('400x200+100+100')
        self.root.title('Cadastro')

        # Criar o objeto View
        self.view = CadastroView(self.root, self)

        #Loop
        self.root.mainloop()
            