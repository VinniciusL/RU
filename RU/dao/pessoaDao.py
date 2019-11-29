from tinydb import TinyDB, Query
from arq.genericDao import GenericDao
from dominio.pessoa import Pessoa
class PessoaDao(GenericDao):

	def __init__(self):
		'''Método construtor da classe PessoaDao'''
		Super().__init__()
		self._table = db.table('pessoa')

	def salvar(self,pessoa):
		'''Método responsável por salvar uma pessoa'''
		self._table.insert({'id':pessoa.id,'nome':pessoa.nome,'cpf':pessoa.cpf,'email':pessoa.email})

	def atualizar(self,field,value,id):
		'''Método responsável por atualizar um campo de uma pessoa'''
		pessoas = self._table.search(where('id') == id)
		for pessoa in pessoas:
			pessoa[field] = value
		self._table.write_back(pessoas)

	def remover(self,id):
		'''Método responsável por remover uma pessoa'''
		self._table.remove(where('id') == id)

	def listar(self):
		'''Método responsável por listar todas as pessoas'''
		return self._table.all()

	def findByCpf(self, cpf):
		'''Método que procura uma pessoa a partir do cpf informado'''
		pessoas = self._table.search(where('cpf') == cpf)
		return pessoas[0]