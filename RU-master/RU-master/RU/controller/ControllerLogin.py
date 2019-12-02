#Classe do controlador

import tkinter as tk
from LoginView import LoginView
from genericDao import GenericDao


class Controller:

    def __init__(self):
        # Criar a Janela principal
        self.root = tk.Tk()
        self.root.geometry('400x200+100+100')
        self.root.title('Login')

        # Criar o objeto View
        self.view = LoginView(self.root, self)

        #Loop
        self.root.mainloop()
