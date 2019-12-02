from arq.genericDao import GenericDao
from dominio.porcao import Porcao
from tinydb import TinyDB, Query

class PorcaoDao(GenericDao):
	'''Classe que representa o dao de uma porção'''
	def __init__(self):
		'''Método construtor da classe PorcaoDao'''
		Super().__init__('porcao')

	def salvar(self, usuario):
		'''Método responsável por salvar uma porção'''
		Super().salvar({'id':porcao.id,'denominacao':denominacao})

	def atualizar(self,field,value,id):
		'''Método responsável por atualizar um campo de uma porção'''
		Super().atualizar(field,value,id)

	def remover(self,id):
		'''Método responsável por remover uma porção'''
		Super().remover(id)

	def listar(self):
		'''Método responsável por listar todos as porções'''
		return Super().listar()

	def findByDenominacao(self,denominacao):
		'''Método que busca um porção a partir de sua denominação'''
		porcoes = self.table.search(where('denominacao') == denominacao)
		return porcoes[0]