from arq.genericService import GenericService
from dominio.pessoa import Pessoa
from dao.pessoaDao import PessoaDao

class PessoaService(GenericService):
	'''Classe que representa um service de pessoa'''

	def __init__(self):
		'''Método construtor da classe PessoaDao'''
		Super().__init__(PessoaDao())

	def salvar(self, pessoa):
		'''Método responsável por salvar uma nova pessoa'''
		if self._dao.findByCpf(pessoa.cpf) is not None:
			raise Exception('Já existe uma pessoa com o cpf cadastrado.')
		else:
			self._dao.salvar(pessoa)

	def atualizar(self, pessoa):
		'''Método resposável por atualizar uma pessoa'''
		pessoaDb = self._dao.findByCpf(pessoaCpf)
		data = {}
		
		if pessoa.nome != pessoaDb.nome:
			data['nome'] = pessoa.nome
		
		if pessoa.email != pessoaDb.email
			data['email'] = pessoa.email

		for field in data:
			self._dao.atualizar(field,data[field],pessoa.id)

	def remover(self, pessoa):
		'''Método responsável por remover uma pessoa'''
		if self._dao.findByCpf(pessoa.cpf) is not None:
			self._dao.remover(pessoa.id)
		else:
			raise Exception('A pessoa informada não se encontra na base de dados.')

	def listar(self):
		'''Método resposável por listar todas a pessoas'''
		return self._dao.listar()