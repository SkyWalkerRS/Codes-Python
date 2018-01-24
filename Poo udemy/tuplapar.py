def tuplaPar(tupla):
	lista = []
	i = 0
	for palavra in tupla:
		if i%2==0:
			lista.append(palavra)
		i+=1	
	print(lista)		



tupla = 'oi','olar','nois','tchau'

tuplaPar(tupla)