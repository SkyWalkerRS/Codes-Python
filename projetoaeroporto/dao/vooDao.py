from models.Voo import Voo
from modelsDao.modelosDao import Metodos
class VooDao(Metodos):
    #o primeiro passo é somente ser executado
    #se receber uma conexão com o banco de dados
    def __init__(self,conexao):
        self.conexao = conexao


    def cadastrar(self,voo):
        sql = ''
        sql = 'INSERT INTO VOO (NUMERO,ORIGEM,DESTINO,LUGARES) \
        VALUES (?,?,?,?)'
        
        self.conexao.execute(sql,(voo.numero,voo.origem,voo.destino,voo.lugares))
        self.conexao.commit()

        

    def alterar(self,voo): 
            sql = 'UPDATE VOO SET NUMERO = ?,ORIGEM = ?,DESTINO = ?,LUGARES = ? \
        WHERE IDEN = ? '
            self.conexao.execute(sql,
                (voo.numero,voo.origem,voo.destino,voo.lugares,voo.iden))
            self.conexao.commit()
        
            
    def listar(self):
        lista = []
        sql = 'SELECT * from VOO'
        resultado = self.conexao.execute(sql)
        for valor in resultado:
            voo = Voo(valor[0],valor[1],valor[2],valor[3],valor[4])
            lista.append(voo)
        return lista

    def getId(self,parametro):
        sql = 'SELECT * from VOO where iden = ?'
        resultado = self.conexao.execute(sql, (parametro,) )
        lista = []
        for valor in resultado:
            voo = Voo(valor[0],valor[1],valor[2],valor[3],valor[4])
            lista.append(voo)
        return lista
        


    def getNum(self,parametro):
        sql = 'SELECT * from VOO where numero = ?'
        resultado = self.conexao.execute(sql, (parametro,) )
        lista = []
        for valor in resultado:
            voo = Voo(valor[0],valor[1],valor[2],valor[3],valor[4])
            lista.append(voo)
        return lista 


    def getOrigem(self,parametro):
        sql = 'SELECT * from VOO where origem = ?'
        resultado = self.conexao.execute(sql, (parametro,) )
        lista = []
        for valor in resultado:
            voo = Voo(valor[0],valor[1],valor[2],valor[3],valor[4])
            lista.append(voo)
        return lista


    def getDestino(self,parametro):
        sql = 'SELECT * from VOO where destino = ?'
        resultado = self.conexao.execute(sql, (parametro,) )
        lista = []
        for valor in resultado:
            voo = Voo(valor[0],valor[1],valor[2],valor[3],valor[4])
            lista.append(voo)
        return lista

    def getLugares(self,parametro):
        sql = 'SELECT * from VOO where lugares = ?'
        resultado = self.conexao.execute(sql, (parametro,) )
        lista = []
        for valor in resultado:
            voo = Voo(valor[0],valor[1],valor[2],valor[3],valor[4])
            lista.append(voo)
        return lista                                      

    def excluir (self,parametro):
        sql = 'DELETE from VOO \
        WHERE IDEN = ?'
        self.conexao.execute(sql, (parametro,) )
        self.conexao.commit()

    
    def deletarTudo (self):
        sql = 'DELETE from VOO \
        WHERE IDEN '
        self.conexao.execute(sql, )
        self.conexao.commit()    

     
    def efetuarReserva(self,numero):
        sql = 'SELECT * from VOO \
        WHERE numero = ?'
        a = ''
        resultado = self.conexao.execute(sql, (numero,) )
        for i in resultado:
            if numero == i[1]:
                x = int(i[4])
                if x > 0:
                    x -=1
                    self.conexao.execute("UPDATE VOO SET LUGARES = ? WHERE numero = ?",(x,numero))
                    self.conexao.commit()
                    a =  "Reserva Confirmada"
                 
                else:
                    a =  "Voo lotado"
            
            else:
                a =  "Voo não existe"
            return a          
           