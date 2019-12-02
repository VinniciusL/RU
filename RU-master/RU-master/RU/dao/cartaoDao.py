from arq.genericDao import GenericDao
from dominio.cartao import Cartao
from tinydb import TinyDB, Query

class CartaoDao(GenericDao):
	'''Classe que representa o dao de cartão'''

	def __init__(self):
		'''Método construtor da classe CartaoDao'''
		Super().__init__('cartao')

	def salvar(self,cartao):
		'''Método responsável por salvar um novo cartão'''
		Super().salvar({'id':cartao.id, 'codigo':cartao.codigo,'saldo':cartao.saldo, 'usuario':cartao.usuario})

	def atualizar(self,field,value,id):
		'''Método responsável por atualizar um campo de um cartão'''
		Super().atualizar(field,value,id)
	def remover(self,id):
		'''Método responsável por remover um cartão'''
		Super().remover(id)

	def listar(self):
		'''Método responsável por listar todos os cartões'''
		return Super().listar()	

	def findByCodigo(self,codigo):
		'''Método resposável por buscar um cartão de acordo com código informado'''
		return self.table.search(where('codigo') == codigo)[0]

	def findByUsuario(self,usuario):
		'''Método responsável por buscar um cartão do usuário'''
		return self.table.search(where('usaurio') == usuario)