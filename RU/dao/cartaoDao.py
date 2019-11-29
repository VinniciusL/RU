from arq.genericDao import GenericDao
from dominio.cartao import Cartao
from tinydb import TinyDB, Query

class CartaoDao(GenericDao):
	'''Classe que representa o dao de cartão'''

	def __init__(self):
		'''Método construtor da classe CartaoDao'''
		Super().__init__()
		self._table = self.db.table('cartao')

	def salvar(self,cartao):
		'''Método responsável por salvar um novo cartão'''
		self._table.insert({'id':cartao.id, 'codigo':cartao.codigo,'saldo':cartao.saldo, 'usuario':cartao.usuario})

	def atualizar(self,field,value,id):
		'''Método responsável por atualizar um campo de um cartão'''
		query = Query()
		cartoes = self._table.search(where('id') == id)
		for cartao in cartoes:
			cartao[field] = value
		self._table.write_back(cartoes)

	def remover(self,id):
		'''Método responsável por remover um cartão'''
		self._table.remove(where('id') == id)

	def listar(self):
		'''Método responsável por listar todos os cartões'''
		return self._table.all()	