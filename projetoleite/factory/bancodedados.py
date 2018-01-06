import sqlite3
from pattern.conexaofactorypattern import ConexaoFactoryPattern
class ConexaoFactory(ConexaoFactoryPattern):

	def __init__(self):
		self.conexao = sqlite3.connect('elegebd.db')
		self.criarTabelas()


	def getConexao(self):
		return self.conexao

	def criarTabelas(self):
		self.conexao.execute('''CREATE TABLE IF NOT EXISTS TANQUE
		(COD INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
		COR TEXT NOT NULL,
		CAPACIDADE REAL NOT NULL,
		TIPO TEXT NOT NULL,
		CARGA REAL)''' )

		self.conexao.execute('''CREATE TABLE IF NOT EXISTS USUARIO
			(COD INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
			LOGIN TEXT NOT NULL,
			SENHA TEXT NOT NULL)''')

	def inicializarDados(self,valida):
		sql = ''
		if valida == True:
			sql = 'INSERT INTO USUARIO (LOGIN,SENHA)\
			VALUES (?,?)'
			self.conexao.execute(sql,('admin','admin'))	
		else:
			sql = 'DELETE FROM USUARIO\
			WHERE LOGIN = ? '
			self.conexao.execute(sql,("admin"))
		self.conexao.commit()	
			