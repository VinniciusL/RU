from arq.genericService import GenericService
from dominio.cartao import Cartao
from dominio.usuario import Usuario
from dao.cartaoDao import CartaoDao

class CartaoService(GenericService):

	def __init__(self):
		'''Método construtor da classe CartaoService'''
		Super().__init__(CartaoDao())

	def salvar(self,cartao):
		'''Método reponsável por cadastrar um cartão'''
		if self.dao.findByCodigo(cartao.codigo) is not None:
			raise Exception('Já existe um cartão cadastrado com o código informado.')

		if self.dao.findByUsuario(cartao.usuario) is not None:
			raise Exception('O usuário informado já possui um cartão.')

		self.dao.salvar(cartao)

	def atualizar(self,cartao):
		'''Método reponsável por cadastrar um cartão'''
		if self.dao.findByCodigo(cartao.codigo) is None:
			cartaoDb = self.dao.findById(cartao.id)
			data = {}

			if cartao.codigo != cartaoDb.codigo:
				data['codigo'] = cartao.codigo

			if cartao.saldo != cartaoDb.saldo:
				data['saldo'] = cartao.saldo

			for field in data:
				self.dao.atualizar(field,data[field],cartao.id)
		else:
			raise Exception('Já existe um cartão cadastrado com o código informado.')