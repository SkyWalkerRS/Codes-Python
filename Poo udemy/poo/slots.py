#Quando há muitas instâncias, é bom usar os slots p/ gastar menos memória

class Carro():
	__slots__ = ['marca','nome','ano']
	def __init__(marca,nome,ano):
		self.marca = marca
		self.nome = nome
		self.ano = ano
		