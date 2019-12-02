from dao.porcaoDao import PorcaoDao
from arq.genericService import GenericService
from dominio.porcao import Porcao

class PorcaoService(GenericService):
	'''Classe que representa o service de porção'''

	def __init__(self):
		'''Método construtor da classe PorcaoService'''
		Super().__init__(PorcaoDao())

	def salvar(self,porcao):
		'''Método responsável por salvar uma porção'''
		if self.dao.findByDenominacao(porcao.denominacao) is None:
			self.dao.salvar(porcao)
		else:
			raise Exception('Já existe uma porção cadastrada com a denominação informada.')

	def atualizar(self, porcao):
		'''Método responsável por atualizar os campos de uma porção'''
		porcaoDb = self.dao.findById(porcao.id)
		data = {}

		if self.dao.findByDenominacao(porcao.denominacao) is None:
			if porcao.denominacao != porcaoDb.denominacao:
				data['denominacao'] = porcao.denominacao

			for field in data:
				self.dao.atualizar(field,data[field],porcao.id)
		else:
			raise Exception('Já existe uma porção cadastrada com a denominação informada.')

	def remover(self,porcao):
		'''Método responsável por remover uma porção'''
		if self.dao.findById(porcao.id) is not None:
			self.dao.remover(porcao.id)
		else:
			raise Exception('A porção informada não se encontra na base de dados.')

	def listar(self):
		'''Método responsável por listar todas as porções'''
		return self.dao.listar()