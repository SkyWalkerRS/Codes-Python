from pattern.tanquedaopattern import TanqueDaoPattern
from models.tanque import Tanque
class TanqueDao(TanqueDaoPattern):
    def __init__(self,conexao):
        self.conexao = conexao

    
    def saveOrUpdate(self,tanque,aux):
        sql = ''
        if aux == True:
            sql = 'INSERT INTO TANQUE (COR,CAPACIDADE,TIPO,CARGA) \
            VALUES (?,?,?,?)'
            
            self.conexao.execute(sql,(tanque.cor,tanque.capacidade,tanque.tipo,tanque.carga))
        else:
            sql = 'UPDATE TANQUE SET COR = ?,CAPACIDADE = ?, TIPO = ?, CARGA = ? WHERE COD = ?'
            self.conexao.execute(sql,(tanque.cor,tanque.capacidade,tanque.tipo,tanque.carga,tanque.cod))   
        self.conexao.commit()	

    def getTanque(self,pesquisa,value):
        lista = []
        
        sql = 'SELECT * FROM TANQUE WHERE '+pesquisa+' = ?'
        print(sql)
        busca = self.conexao.execute(sql,(value,))
        for i in busca:
            t = Tanque(i[0],i[1],i[2],i[3],i[4])
            lista.append(t)
        return lista
        

       

    def excluir(self,tanque):
        sql = 'DELETE FROM TANQUE WHERE COD = ?'
        self.conexao.execute(sql,(tanque,))
        self.conexao.commit()	

        

    def getLista(self):
        lista = []
        sql = "SELECT * FROM TANQUE"
        busca = self.conexao.execute(sql)
        for i in busca:
            t = Tanque(i[0],i[1],i[2],i[3],i[4])
            lista.append(t)
        return lista    


    def getListaPesquisa(self,tanque):
        lista = []
        sql = 'SELECT * FROM TANQUE WHERE COD = ?'
        busca = self.conexao.execute(sql,(tanque,))
        for i in busca:
            t = Tanque(i[0],i[1],i[2],i[3],i[4])
            lista.append(t)
        return lista    


    def getCarga(self,tanqueCod,retirar):
        tanque=self.getListaPesquisa(tanqueCod)        
        if(len(tanque)): 
            if(tanque[0].carga - retirar>=0):
               tanque[0].carga = tanque[0].carga - retirar
               tanque[0].cod = tanqueCod
               self.saveOrUpdate(tanque[0],False)
               return 0
            else:
                return -2
        else:
            return -1
               

    def setCarga(self,tanqueCod,deposito):
        tanque=self.getListaPesquisa(tanqueCod)
        if(len(tanque)):
            
            capacidade = tanque[0].capacidade
            carga = tanque[0].carga

            if(tanque[0].tipo =="Pasteurizado"):
                capacidade = capacidade - (capacidade*10)/100
            if(tanque[0].tipo == "Semi Desnatado"):
                capacidade = capacidade - (capacidade*5)/100
            if(capacidade< tanque[0].carga+deposito):
                
                
                x = (carga*100)/capacidade
                print(x)

                input("press (enter)")
            else:
                print(1,tanque[0].carga)
                tanque[0].carga = tanque[0].carga+deposito
                tanque[0].cod = tanqueCod
                print(2,tanque[0].carga)
                self.saveOrUpdate(tanque[0],False)
                
                y = (carga*100)/capacidade
                print(y)
                input("press (enter)")
        else:
            input("Depósito não poderá ser feito..")
              











	
   
