#Classe do controlador

import tkinter as tk
from CardapioView import CardapioView
from genericDao import GenericDao


class Controller:

    def __init__(self):
        # Criar a Janela principal
        self.root = tk.Tk()
        self.root.geometry('400x200+100+100')
        self.root.title('Cardápio')  


        # Criar o objeto View
        self.view = CardapioView(self.root, self)

        #Loop
        self.root.mainloop()
            
    def listar_cartao(self):
        self.view.listar(Cartao.listar())