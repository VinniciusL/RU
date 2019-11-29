from arq.genericDao import GenericDao
from dominio.porcao import Porcao
from tinydb import TinyDB, Query

class PorcaoDao(GenericDao):
	'''Classe que representa o dao de uma porção'''
	def __init__(self):
		'''Método construtor da classe PorcaoDao'''
		Super().__init__()
		self._table = self.db.table('porcao')

	def salvar(self, usuario):
		'''Método responsável por salvar uma porção'''
		self._table.insert({'id':porcao.id,'denominacao':denominacao})

	def atualizar(self,field,value,id):
		'''Método responsável por atualizar um campo de uma porção'''
		query = Query()
		porcoes = self._table.search(where('id') == id)
		for porcao in porcoes:
			porcao[field] = value
		self._table.write_back(porcoes)

	def remover(self,id):
		'''Método responsável por remover uma porção'''
		self._table.remove(where('id') == id)

	def listar(self):
		'''Método responsável por listar todos as porções'''
		return self._table.all()