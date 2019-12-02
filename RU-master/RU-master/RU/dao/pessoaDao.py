from tinydb import TinyDB, Query
from arq.genericDao import GenericDao
from dominio.pessoa import Pessoa
class PessoaDao(GenericDao):

	def __init__(self):
		'''Método construtor da classe PessoaDao'''
		Super().__init__('pessoa')
		
	def salvar(self,pessoa):
		'''Método responsável por salvar uma pessoa'''
		Super().salvar({'id':pessoa.id,'nome':pessoa.nome,'cpf':pessoa.cpf,'email':pessoa.email})

	def atualizar(self,field,value,id):
		'''Método responsável por atualizar um campo de uma pessoa'''
		Super().atualizar(field,value,id)

	def remover(self,id):
		'''Método responsável por remover uma pessoa'''
		Super().remover(id)

	def listar(self):
		'''Método responsável por listar todas as pessoas'''
		return Super().listar

	def findByCpf(self, cpf):
		'''Método que procura uma pessoa a partir do cpf informado'''
		pessoas = self._table.search(where('cpf') == cpf)
		return pessoas[0]