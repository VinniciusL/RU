#Classe do controlador

import tkinter as tk
from HistoricoView import HistoricoView
# from genericDao import GenericDao


class Controller:
    '''
    O controlador define 2 ações:
     - adicionar_pessoa: para adicionar novas pessoas no banco de
       dados.  
     - listar_pessoas: retornar a lista das pessoas

     Note que as 2 ações supracitadas utilizam a classe do Modelo para
     consultar/atualizar o banco de dados
    '''

    def __init__(self):
        # Criar a Janela principal
        self.root = tk.Tk()
        self.root.geometry('400x200+100+100')
        self.root.title('Histórico de Compras')  


        # Criar o objeto View
        self.view = HistoricoView(self.root, self)

        #Loop
        self.root.mainloop()
