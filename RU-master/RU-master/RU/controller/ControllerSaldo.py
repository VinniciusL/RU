#Classe do controlador

import tkinter as tk
from SaldoView import SaldoView
from genericDao import GenericDao


class Controller:


    def __init__(self):
        # Criar a Janela principal
        self.root = tk.Tk()
        self.root.geometry('400x200+100+100')
        self.root.title('Saldo')  


        # Criar o objeto View
        self.view = SaldoView(self.root, self)

        #Loop
        self.root.mainloop()
                   
    def mostrar_saldo(self):
        self.view.saldo(Saldo.mostrar())