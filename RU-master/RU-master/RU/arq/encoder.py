import json
from dominio.pessoa import Pessoa
from dominio.usuario import Usuario
from dominio.cartao import Cartao
from dominio.porcao import Porcao
from dominio.refeicao import Refeicao

class Enconder(json.JSONEncoder):

	def default(self, atributos):
		dic = vars(atributos)
		dic['tipo'] = atributos.__class__.__name__
		return dic

	@staticmethod
	def decode(dic):
		if dic['tipo'] == 'Pessoa':
			return Pessoa(dic['_id'],dic['_nome'],dic['_cpf'],dic['_email'])
		
		if dic['tipo'] == 'Usuario':
			return Usuario(dic['_id'],dic['_login'],dic['_senha'],dic['_ativo'],dic['_pessoa'])

		if dic['tipo'] == 'Cartao':
			return Cartao(dic['_id'],dic['_codigo'],dic['_saldo'],dic['_usuario'])

		if dic['tipo'] == 'Porcao':
			return Porcao(dic['_id'],dic['_denominacao'])

		if dic['tipo'] == 'Refeicao':
			return Refeicao(dic['_id'],dic['_denominacao'],dic['_porcoes'])