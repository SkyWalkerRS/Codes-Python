


def numeroPerfeito(num):
	'''Se a soma de todos os divisores do número for o próprio número, retornará True..'''
	i = 1
	lista = []
	while num > i:
		if num % i == 0:
			lista.append(i)
		i+=1
	if sum(lista) == num:
		return True
	else:
		return False
num = 28
print(numeroPerfeito(num))
print(help(numeroPerfeito))							
    
    
