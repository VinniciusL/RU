#Classe do controlador

import tkinter as tk
from RecargaView import RecargaView
# from genericDao import GenericDao




class Controller:

    def __init__(self):
        # Criar a Janela principal
        self.root = tk.Tk()
        self.root.geometry('400x200+100+100')
        self.root.title('Recarga de Cartão')  



        # Criar o objeto View
        self.view = RecargaView(self.root, self)

        #Loop
        self.root.mainloop()
            