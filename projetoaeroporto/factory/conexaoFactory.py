import sqlite3

class ConexaoFabrica():

    def __init__(self):
        self.conexao = sqlite3.connect('banco de dados.db')
        self.criarTabelaVoo()
        self.criarTabelaAeroporto()
        self.criarTabelaPassageiro()

    def getConexao(self):
        return self.conexao
    
    def criarTabelaVoo(self):
        self.conexao.execute('''CREATE TABLE IF NOT EXISTS VOO
        (IDEN INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NUMERO TEXT NOT NULL,
        ORIGEM TEXT NOT NULL,
        DESTINO TEXT NOT NULL,
        LUGARES INTEGER)''')

    
    def criarTabelaAeroporto(self):
        self.conexao.execute('''CREATE TABLE IF NOT EXISTS AEROPORTO
        (IDEN INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NOME TEXT NOT NULL,
        SIGLA TEXT NOT NULL)''')

      
    def criarTabelaPassageiro(self):
        self.conexao.execute('''CREATE TABLE IF NOT EXISTS PASSAGEIRO
        (IDEN INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NOME TEXT NOT NULL,
        CPF TEXT NOT NULL,
        IDADE INTEGER)''')

       
    
