
class Voo():
	def __init__(self,iden,numero,origem,destino,lugares):
		self.iden = iden
		self.numero = numero
		self.origem = origem
		self.destino = destino
		self.lugares = lugares



	def __str__(self):
		return "Número: " + self.numero + " Origem: " + self.origem + " Destino: " + self.destino + " Nº de lugares " + (str(self.lugares))
	

	@property
	def origem(self):
		return self._origem
	@origem.setter
	def origem(self,value):
		self._origem = value.capitalize()

	@property
	def destino(self):
		return self._destino
	@destino.setter
	def destino(self,value):
		self._destino = value.capitalize()

	'''@property
	def lugares(self):
		return self._lugares
	@lugares.setter
	def lugares(self,value):
		if value <= 0:
			self._lugares = 15
		else:
			self._lugares = value	
'''


























