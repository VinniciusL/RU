from arq.genericService import GenericService
from dominio.usuario import Usuario
from dao.usuarioDao import UsuarioDao
from service.pessoaService import PessoaService

class UsuarioService(GenericService):
	'''Classe que representa o service de usuário'''

	def __init__(self):
		'''Método contrutor da classe UsuarioDao'''
		Super().__init__(UsuarioDao())

	def salvar(self,usuario):
		'''Método responsável por salvar um novo usuário'''
		if self._dao.findByLogin(usuario.login) is None:
			self._dao.salvar(usuario)
		else:
			raise Exception('Já existe um usuário com o login informado')

	def atualizar(self, usuario):
		'''Método responsável por atualizar um usuário'''

		pessoaService = PessoaService()
		pessoaService.atualizar(usuario.pessoa)

		usuarioDb = self._dao.findById('usuario',usuario.id)
		data{}

		if usuario.login != usuarioDb.login:
			data['login'] = usuario.login

		if usuario.senha != usuarioDb.senha:
			data['senha'] = usuario.senha

		if usuario.vinculo != usuarioDb.vinculo:
			data['vinculo'] = usuario.vinculo

		if usuario.ativo != usuarioDb.ativo:
			data['ativo'] = usuario.ativo

		for field in data:
			self._dao.atualizar(field,data[field],usuario.id)

	def remover(self, usuario):
		'''Método responsável por remover um usuário'''
		if self._dao.findById('usuario',usuario.id) is not None:
			self._dao.remover(usuario.id)
			pessoaService = PessoaService()
			pessoaService.remover(usuario.pessoa.cpf)

		else:
			raise Exception('Usuario informado não se encontra na base de dados.')

	def listar(self):
		'''Método responsável por listar todos os usuários'''
		return self._dao.listar()