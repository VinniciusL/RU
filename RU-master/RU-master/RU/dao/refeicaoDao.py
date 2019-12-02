from arq.genericDao import GenericDao
from dominio.refeicao import Refeicao
from tinydb import TinyDB, Query

class RefeicaoDao(GenericDao):
	'''Classe que representa o dao de refeição'''

def __init__(self):
		'''Método construtor da classe RefeicaoDao'''
		Super().__init__('refeicao')

	def salvar(self,refeicao):
		'''Método responsável por salvar uma nova refeição'''
		Super().salvar({'id':refeicao.id,'denominacao':refeicao.denominacao,'porcoes':refeicao.porcoes})

	def atualizar(self,field,value,id):
		'''Método responsável por atualizar um campo de uma refeição'''
		Super().atualizar(field,value,id)

	def remover(self,id):
		'''Método responsável por remover uma refeição'''
		Super().remover(id)

	def listar(self):
		'''Método responsável por listar todos as refeições'''
		return Super().listar

	def findByDenominacao(self,denominacao):
		'''Método que busca uma refeição de acordo com a denominação informada'''
		return self.table.search(where('denominacao') == denominacao)[0]