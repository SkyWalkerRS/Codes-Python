class Tanque():
	def __init__(self,cod,cor,capacidade,tipo,carga):
		self.cod = cod
		self.cor = cor
		self.capacidade = capacidade
		self.tipo = tipo
		self.carga = carga
	


	def __str__(self):
		return "Cod:" + str(self.cod)+ ' | ' + 'Cor:'+  self.cor + ' | ' + " Capacidade:" + str(self.capacidade) + ' | '+ " Tipo:" + self.tipo + ' | ' + " Carga:" + str(self.carga)

	'''@property
	def capacidade(self):
		return self._capacidade
        3

	@capacidade.setter
	def capacidade(self,value):
		if value == "Pasteurizado":
			self._capacidade = self._capacidade * 0.90
		else:
			pass'''			

