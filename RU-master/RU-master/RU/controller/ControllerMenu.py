#Classe do controlador

import tkinter as tk
from MenuView import MenuView
from genericDao import GenericDao


class Controller:

    def __init__(self):
        # Criar a Janela principal
        self.root = tk.Tk()
        self.root.geometry('400x200+100+100')
        self.root.title('Menu do Usuário')

        # Criar o objeto View
        self.view = MenuView(self.root, self)

        #Loop
        self.root.mainloop()