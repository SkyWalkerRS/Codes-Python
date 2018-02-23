class SomentePares(list):

	def append(self, inteiro):

		if not isinstance(inteiro, int):
			raise TypeError('Somente inteiros')
		if inteiro % 2:
			raise ValueError('Somente pares')

		super().append(inteiro)


sp = SomentePares()
sp.append(10)
sp.append(20)
sp.append(4)