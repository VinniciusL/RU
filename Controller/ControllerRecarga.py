#Classe do controlador

import tkinter as tk
from RecargaView import RecargaView
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
        self.root.title('Recarga de Cartão')  



        # Criar o objeto View
        self.view = RecargaView(self.root, self)

        #Loop
        self.root.mainloop()
            