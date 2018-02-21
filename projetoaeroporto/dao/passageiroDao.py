from models.Passageiro import Passageiro
from modelsDao.modelosDao import Metodos
class PassageiroDao(Metodos):
    #o primeiro passo é somente ser executado
    #se receber uma conexão com o banco de dados
    def __init__(self,conexao):
        self.conexao = conexao


    def cadastrar(self,passageiro):
        sql = ''
        sql = 'INSERT INTO PASSAGEIRO (NOME,CPF,IDADE) \
        VALUES (?,?,?)'
        self.conexao.execute(sql,(passageiro.nome,passageiro.cpf,passageiro.idade))
        self.conexao.commit()




    def alterar(self,passageiro): 
            sql = 'UPDATE PASSAGEIRO SET NOME = ?,CPF = ?,IDADE =? \
        WHERE IDEN = ? '
            self.conexao.execute(sql,
                (passageiro.nome,passageiro.cpf,passageiro.idade,passageiro.iden))
            self.conexao.commit()        



    def listar(self):
        lista = []
        sql = 'SELECT * from PASSAGEIRO'
        resultado = self.conexao.execute(sql)
        for valor in resultado:
            passageiro = Passageiro(valor[0],valor[1],valor[2],valor[3])
            lista.append(passageiro)
        return lista

    def getId(self,parametro):
        lista = []
        sql = 'SELECT * from PASSAGEIRO where iden = ?'
        resultado = self.conexao.execute(sql, (parametro,) )
        for valor in resultado:
            passageiro = Passageiro(valor[0],valor[1],valor[2],valor[3])
            lista.append(passageiro)
        return lista


    def getNome(self,parametro):
        lista = []
        sql = 'SELECT * from PASSAGEIRO where nome = ?'
        resultado = self.conexao.execute(sql, (parametro,) )
        for valor in resultado:
            passageiro = Passageiro(valor[0],valor[1],valor[2],valor[3])
            lista.append(passageiro)
        return lista


    
    def getCpf(self,parametro):
        lista = []
        sql = 'SELECT * from PASSAGEIRO where cpf = ?'
        resultado = self.conexao.execute(sql, (parametro,) )
        for valor in resultado:
            passageiro = Passageiro(valor[0],valor[1],valor[2],valor[3])
            lista.append(passageiro)
        return lista

    

    def getIdade(self,parametro):
        lista = []
        sql = 'SELECT * from PASSAGEIRO where idade = ?'
        resultado = self.conexao.execute(sql, (parametro,) )
        for valor in resultado:
            passageiro = Passageiro(valor[0],valor[1],valor[2],valor[3])
            lista.append(passageiro)
        return lista            

    def excluir (self,parametro):
        sql = 'DELETE from PASSAGEIRO \
        WHERE IDEN = ?'
        self.conexao.execute(sql, (parametro,) )
        self.conexao.commit()



    def deletarTudo (self):
        sql = 'DELETE from PASSAGEIRO \
        WHERE IDEN '
        self.conexao.execute(sql, )
        self.conexao.commit()        