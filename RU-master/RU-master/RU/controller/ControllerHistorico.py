#Classe do controlador

import tkinter as tk
from HistoricoView import HistoricoView
from genericDao import GenericDao


class Controller:

    def __init__(self):
        # Criar a Janela principal
        self.root = tk.Tk()
        self.root.geometry('400x200+100+100')
        self.root.title('Histórico de Compras')  


        # Criar o objeto View
        self.view = HistoricoView(self.root, self)

        #Loop
        self.root.mainloop()
