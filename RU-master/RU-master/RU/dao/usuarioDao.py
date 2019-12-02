from arq.genericDao import GenericDao
from dominio.usuario import Usuario
from tinydb import TinyDB, Query

class UsuarioDao(GenericDao):
	'''Classe que representa o dao de usuário'''
	def __init__(self):
		'''Método construtor da classe UsuarioDao'''
		Super().__init__('usuario')

	def salvar(self, usuario):
		'''Método responsável por salvar um usuário'''
		Super().salvar({'id':usuario.id, 'login':usuario.login, 'senha':usuario.senha, 'vinculo':usuario.vinculo, 'ativo':usuario.ativo}, 'pessoa':usuario.pessoa)

	def atualizar(self,field,value,id):
		'''Método responsável por atualizar um campo de um usuário'''
		Super().atualizar(field,value,id)

	def remover(self,id):
		'''Método responsável por remover um usuário'''
		Super().remover(id)

	def listar(self):
		'''Método responsável por listar todos os usuários'''
		return Super().listar

	def findByLogin(self,login):
		'''Método responsável por procurar um usuário através do login informado'''
		usuarios = self._table.search(where('login') == login)
		return usuarios[0]

	