from abc import ABC, abstractmethod
from tinydb import TinyDB, Query

class GenericDao(ABC):
	'''Classe que representa um DAO genérico'''
	def __init__(self,table):
		self._db = TinyDB('db.json')
		self._table = self._db.table(table)

	def salvar(self, dados):
		'''Método responsável por salvar os dados de uma entidade'''
		self.table.insert(dados)

	def atualizar(self,field,value,id):
		'''Método responsável por atualizar um campo de uma entidade'''
		lista = self._table.search(where('id' == id))
		for linha in lista:
			linha[field] = value
		self._table.write_back(lista)

	def remover(self,id):
		'''Método responsável por remover um elemento de uma lista'''
		self._table.remove(where('id') == id)

	def listar(self):
		'''Método responável por listar todos os elementos de uma tabela'''
		return self._table.all()

	def findById(self,table,id):
		'''Método responsável por buscar uma entidade através do id'''
		dados = self._table.search(where('id') == id)
		return dados[0]

	@property
	def db(self):
		return self._db
	
	@property
	def table(self):
		return self._table


if __name__ == "__main__":
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            connection.connect((HOST, PORT))
            print("Conectado!")
            
            client = Cliente(connection)
            for i in range(10):
                #Enviar/adicionar produtos
                client.enviarProduto()
                # Receber a lista do servidor
                lista = client.receberLista()
                print('--------------')
                for l in L:
                    print(l)
                print('--------------')
                time.sleep(random.uniform(0.1,3))

            #Fim
            client.terminar()
            print('Fim do cliente')
    
    except Exception as E:
        print('Erro na conexao...{0}'.format(E))
        raise E