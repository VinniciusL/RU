from arq.genericDao import GenericDao
from dominio.usuario import Usuario
from tinydb import TinyDB, Query

class UsuarioDao(GenericDao):
	'''Classe que representa o dao de usuário'''
	def __init__(self):
		'''Método construtor da classe UsuarioDao'''
		Super().__init__()
		self._table = self.db.table('usuario')

	def salvar(self, usuario):
		'''Método responsável por salvar um usuário'''
		self._table.insert({'id':usuario.id, 'login':usuario.login, 'senha':usuario.senha, 'vinculo':usuario.vinculo, 'ativo':usuario.ativo}, 'pessoa':usuario.pessoa)

	def atualizar(self,field,value,id):
		'''Método responsável por atualizar um campo de um usuário'''
		query = Query()
		usuarios = self._table.search(where('id') == id)
		for usuario in usuarios:
			usuario[field] = value
		self._table.write_back(usuario)

	def remover(self,id):
		'''Método responsável por remover um usuário'''
		self._table.remove(where('id') == id)

	def listar(self):
		'''Método responsável por listar todos os usuários'''
		return self._table.all()

	def findByLogin(self,login):
		'''Método responsável por procurar um usuário através do login informado'''
		query = Query()
		usuarios = self._table.search(where('login') == login)
		return usuarios[0]

	