class Aeroporto():
	def __init__(self,iden,nome,sigla):
		self.iden = iden
		self.nome = nome
		self.sigla = sigla
	def __str__(self):
		return "Nome: " + self.nome  + " Sigla: " + self.sigla


	@property
	def nome(self):
		return self._nome

	@nome.setter
	def nome(self,value):
		self._nome = value.upper()

	@property
	def sigla(self):
		return self._sigla

	@sigla.setter
	def sigla(self,value):
		self._sigla = value.upper()				


