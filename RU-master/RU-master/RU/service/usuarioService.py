from arq.genericService import GenericService
from dominio.usuario import Usuario
from dao.usuarioDao import UsuarioDao
from service.pessoaService import PessoaService

class UsuarioService(GenericService):
	'''Classe que representa o service de usuário'''

	def __init__(self):
		'''Método contrutor da classe UsuarioService'''
		Super().__init__(UsuarioDao())

	def salvar(self,usuario):
		'''Método responsável por salvar um novo usuário'''
		if self.dao.findByLogin(usuario.login) is None:
			self.dao.salvar(usuario)
		else:
			raise Exception('Já existe um usuário cadastrado com o login informado.')

	def atualizar(self, usuario):
		'''Método responsável por atualizar um usuário'''
		if self.dao.findByLogin(usuario.login) is None:
			pessoaService = PessoaService()
			pessoaService.atualizar(usuario.pessoa)

			usuarioDb = self.dao.findById(usuario.id)
			data = {}

			if usuario.login != usuarioDb.login:
				data['login'] = usuario.login

			if usuario.senha != usuarioDb.senha:
				data['senha'] = usuario.senha

			if usuario.vinculo != usuarioDb.vinculo:
				data['vinculo'] = usuario.vinculo

			if usuario.ativo != usuarioDb.ativo:
				data['ativo'] = usuario.ativo

			for field in data:
				self.dao.atualizar(field,data[field],usuario.id)
		else:
			raise Exception('Já existe um usuário cadastrado com o login informado.')

	def remover(self, usuario):
		'''Método responsável por remover um usuário'''
		if self.dao.findById('usuario',usuario.id) is not None:
			self.dao.remover(usuario.id)
			pessoaService = PessoaService()
			pessoaService.remover(usuario.pessoa.cpf)

		else:
			raise Exception('Usuario informado não se encontra na base de dados.')

	def listar(self):
		'''Método responsável por listar todos os usuários'''
		return self.dao.listar()