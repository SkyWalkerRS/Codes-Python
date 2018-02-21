'''
Quando utilizar?

1) Se você desejar reutilizar uma determinada feature em várias classes diferentes.
2) Para melhorar a modularidade.

Mixins é uma forma controlada de adicionar funcionalidades as classes.

Propriedades:
1) não deve ser extendida
2) não deve ser instanciada
<<<<<<< HEAD
<<<<<<< HEAD
####
=======
>>>>>>> 58eebfe2eaa34dba6094792e6ed8f1d6a0fe585a

=======
##
>>>>>>> 5e262e6aef1a38337e488c773d06b22cd48e9732
Em Python, o conceito de mixins é implementado utilizando herança múltipla.
'''

class Livro(object):
	def __init__(self, nome, conteudo):
		self.nome = nome
		self.conteudo = conteudo

class LivroHTMLMixin(object):
	def renderizar(self):
		return ('<html><title>%s</title><body>%s</body></html>') % (self.nome, self.conteudo)

class LivroHTML(Livro, LivroHTMLMixin): #herança múltipla
	pass


livro_html = LivroHTML('Algum Livro', 'blablabla')
print(livro_html.renderizar())