from abc, import ABC, abstractmethod

class GenericService(ABC):
	'''Classe que representa um service genérico'''
	def __init__(self, dao):
		'''Método construtor da classe GenericService'''
		self._dao = dao

	@abstractmethod
	def salvar(self, dado):
		'''Método para salvar um dado no banco de dados'''
		pass

	@abstractmethod
	def atualizar(self, field, value, id):
		'''Método para atualizar um campo de determinada entidade no banco de dados'''
		pass

	@abstractmethod
	def remover(self, dado):
		'''Método para remover determinado dado do banco de dados'''
		pass

	@abstractmethod
	def listar(self):
		'''Método para listar todos os dados do banco'''
		pass

	#Métodos getters e setters
	@property
	def dao(self):
		return self._dao
	