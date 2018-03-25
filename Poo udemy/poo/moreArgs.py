'''
def funcao(*args):
	print(args)
'''

def funcao(**kwargs):
	for key, value in kwargs.items():
		print(key,value)

funcao(nome='marcos', idade=28, linguagem='python')