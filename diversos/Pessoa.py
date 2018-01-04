class Pessoa(object):
  
	def __init__(self,nome,sobrenome):
	    self.nome = nome
	    self.sobrenome = sobrenome
	def getNomeCompleto(self):
		return self.nome + " " +  self.sobrenome


nome = 'Kleber'
sobrenome = 'Barilli'
pessoa1 = Pessoa(nome,sobrenome)
print(pessoa1.getNomeCompleto())