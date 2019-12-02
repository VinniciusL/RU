from arq.genericService import GenericService
from dominio.refeicao import Refeicao
from dominio.porcao import Porcao
from dao.refeicaoDao import RefeicaoDao

class RefeicaoService(GenericService):
	'''Classe que representa o service de refeição'''

	def __init__(self):
		'''Método construtor da classe RefeicaoService'''
		Super().__init__(RefeicaoDao())

	def salvar(self,refeicao):
		'''Método responsável por salvar uma refeição'''
		if self.dao.findByDenominacao(refeicao.denominacao) is None:
			self.dao.salvar(refeicao)
		else:
			raise Exception('Já existe uma refeição cadastrada com a denominação informada.')

	def atualizar(self,refeicao):
		'''Método reposável por atualizar os campos de uma refeição'''
		if self.dao.findByDenominacao(refeicao.denominacao) is None:
			refeicaoDb = self.dao.findById(refeicao.id)
			data = {}

			if refeicao.denominacao != refeicaoDb.denominacao:
				data['denominacao'] = refeicao.denominacao

			if refeicao.porcoes != refeicaoDb.porcoes:
				data['porcoes'] = refeicao.porcoes

			for field in data:
				self.dao.atualizar(field,data[field],refeicao.id)

		else:
			raise Exception('Já existe uma refeição cadastrada com denominação informada.')