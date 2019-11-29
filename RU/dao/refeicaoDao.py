from arq.genericDao import GenericDao
from dominio.refeicao import Refeicao
from tinydb import TinyDB, Query

class RefeicaoDao(GenericDao):
	'''Classe que representa o dao de refeição'''

def __init__(self):
		'''Método construtor da classe RefeicaoDao'''
		Super().__init__()
		self._table = self.db.table('refeicao')

	def salvar(self,refeicao):
		'''Método responsável por salvar uma nova refeição'''
		self._table.insert({'id':refeicao.id,'denominacao':refeicao.denominacao,'porcoes':refeicao.porcoes})

	def atualizar(self,field,value,id):
		'''Método responsável por atualizar um campo de uma refeição'''
		query = Query()
		refeicoes = self._table.search(where('id') == id)
		for refeicao in refeicoes:
			refeicao[field] = value
		self._table.write_back(refeicoes)

	def remover(self,id):
		'''Método responsável por remover uma refeição'''
		self._table.remove(where('id') == id)

	def listar(self):
		'''Método responsável por listar todos as refeições'''
		return self._table.all()