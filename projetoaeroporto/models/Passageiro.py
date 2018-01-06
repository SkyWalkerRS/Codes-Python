class Passageiro():
	def __init__(self,iden,nome,cpf,idade):
		self.iden = iden
		self.nome = nome
		self.cpf = cpf
		self.idade = idade
	

	def __str__(self):
		return "Nome: " + self.nome + " CPF: " + self.cpf + " Idade: " + str(self.idade)


	@property
	def nome(self):
		return self._nome
	@nome.setter
	def nome(self,value):
		self._nome = value.capitalize()	



	@property 
	def idade(self):
		return self._idade 

	@idade.setter
	def idade(self,value):
		if value <= 0:
			self._idade = 21
		else:
			self._idade = value


