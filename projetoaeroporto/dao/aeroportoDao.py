from models.Aeroporto import Aeroporto
from modelsDao.modelosDao import Metodos
class AeroportoDao(Metodos):
    #o primeiro passo é somente ser executado
    #se receber uma conexão com o banco de dados
    def __init__(self,conexao):
        self.conexao = conexao

    
    def cadastrar(self,aeroporto):
        sql = ''
        sql = 'INSERT INTO AEROPORTO (NOME,SIGLA) \
        VALUES (?,?)'
        self.conexao.execute(sql,(aeroporto.nome,aeroporto.sigla))
        self.conexao.commit()


    def alterar(self,aero): 
            sql = 'UPDATE AEROPORTO SET NOME = ?,SIGLA = ? \
        WHERE IDEN = ? '
            self.conexao.execute(sql,
                (aero.nome,aero.sigla,aero.iden))
            self.conexao.commit()    


    

    def listar(self):
        lista = []
        sql = 'SELECT * from AEROPORTO'
        resultado = self.conexao.execute(sql)
        for valor in resultado:
            aero = Aeroporto(valor[0],valor[1],valor[2])
            lista.append(aero)
        return lista

    def getId(self,parametro):
        lista = []
        sql = 'SELECT * from AEROPORTO where iden = ?'
        resultado = self.conexao.execute(sql, (parametro,) )
        for valor in resultado:
            aero = Aeroporto(valor[0],valor[1],valor[2])
            lista.append(aero)
        return lista

    def getNome(self,parametro):
        lista = []
        sql = 'SELECT * from AEROPORTO where nome = ?'
        resultado = self.conexao.execute(sql, (parametro,) )
        for valor in resultado:
            aero = Aeroporto(valor[0],valor[1],valor[2])
            lista.append(aero)
        return lista



    def getSigla(self,parametro):
        lista = []
        sql = 'SELECT * from AEROPORTO where sigla = ?'
        resultado = self.conexao.execute(sql, (parametro,) )
        for valor in resultado:
            aero = Aeroporto(valor[0],valor[1],valor[2])
            lista.append(aero)
        return lista                    

    def excluir (self,parametro):
        sql = 'DELETE from AEROPORTO \
        WHERE IDEN = ?'
        self.conexao.execute(sql, (parametro,) )
        self.conexao.commit()




    def deletarTudo (self):
        sql = 'DELETE from AEROPORTO \
        WHERE IDEN '
        self.conexao.execute(sql, )
        self.conexao.commit()    