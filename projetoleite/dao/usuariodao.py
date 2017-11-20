from pattern.usuariodaopattern import UsuarioDaoPattern
from models.usuario import Usuario
class UsuarioDao(UsuarioDaoPattern):

	def __init__(self,conexao):
		self.conexao = conexao

	def saveOrUpdate(self,usuario,aux = True):
		sql = ''
		if aux == True:
			sql = 'INSERT INTO USUARIO (LOGIN,SENHA) \
			VALUES (?,?)'
			self.conexao.execute(sql,(usuario.login,usuario.senha))
		else:
			sql = 'UPDATE USUARIO SET LOGIN = ?, SENHA = ? WHERE COD = ?'
			self.conexao.execute(sql,(usuario.login,usuario.senha,usuario.cod))
		self.conexao.commit()	


	
	def getLista(self):
		lista = []
		sql = 'SELECT * FROM USUARIO'
		busca = self.conexao.execute(sql)
		for i in busca:
			u = Usuario(i[0],i[1],i[2])
			lista.append(u)
		return lista	

	
	def getListaPesquisa(self,usuario):
		lista = []
		sql = 'SELECT * FROM USUARIO WHERE COD = ?'
		busca = self.conexao.execute(sql,(usuario,))
		for i in busca:
			u = Usuario(i[0],i[1],i[2])
			lista.append(u)
		return lista	


	
	def excluir(self,usuario):
		sql = 'DELETE FROM USUARIO WHERE COD = ?'
		self.conexao.execute(sql,(usuario,))
		self.conexao.commit()
