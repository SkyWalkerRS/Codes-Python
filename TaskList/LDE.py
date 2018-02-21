# -- Nodo duplo --
class Dnodo:
    def __init__(self, dado):
        self.dado = dado
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.dado)

    # Métodos de comparacao do Python, aqui deixamos claros de que forma um objeto Dnodo sera comparado
    def __lt__(self, other):
        return self.dado < other.dado
    
    def __le__(self, other):
        return self.dado <= other.dado
        
    def __eq__(self, other):
        if other.dado is None:
            if self is other:
                return True
            else:
                return False
        if (self.dado == other.dado):
            return True
        else:
            return False
        
    def __ne__(self, other):
        if other.dado is None:
            if self is not other:
                return True
            else:
                return False
        if (self.dado != other.dado):
            return True
        else:
            return False
        
    def __gt__(self, other):
        return self.dado > other.dado
        
    def __ge__(self, other):
        return self.dado >= other.dado    

# -- Lista Duplamente Encadeada --
class LDE:
    def __init__(self):
        self.header = Dnodo(None)
        self.trailer = Dnodo(None)
        self.tam = 0

    def vazia(self):
        if self.tam == 0:
            return True
        
        return False

    def inserirInicio(self, item):
        if self.vazia():
            item.next = self.trailer
            self.trailer.prev = item
            
            item.prev = self.header
            self.header.next = item

        else:
            primeiro = self.header.next
            self.header.next = item
            item.prev = self.header
            item.next = primeiro
            primeiro.prev = item

        self.tam += 1
            
    def inserirFim(self, item):
        if self.vazia():
            item.next = self.trailer
            self.trailer.prev = item
            
            item.prev = self.header
            self.header.next = item
        else:
            ultimo = self.trailer.prev
            self.trailer.prev = item
            item.next = self.trailer
            item.prev = ultimo
            ultimo.next = item
            
        self.tam += 1    

    def inserirInicio(self,item):
        if self.vazia():
            item.next = self.trailer
            self.trailer.prev = item
            item.prev = self.header
            self.header.next = item
        else:
            primeiro = self.header.next
            self.header.next = item
            item.prev = self.header
            item.next = primeiro
            primeiro.prev = item
        self.tam += 1

    def inserirFim(self,item):
        if self.vazia():
            item.next = self.trailer
            self.trailer.prev = item
            item.prev = self.header
            self.header.next = item
        else:
            ultimo = self.trailer.prev
            self.trailer.prev = item
            item.prev = ultimo
            item.next = self.trailer
            ultimo.next = item
        self.tam += 1

    def inserirApos(self, alvo, item):
        if self.vazia():
            print("[Lista Vazia]")
            return
        else:
            busca = self.buscar(alvo)
            if(busca.next == self.trailer):
                self.inserirFim(item)                            
            else:
                atual = busca.next
                busca.next = item
                item.prev = busca
                item.next = atual
                atual.prev = item
                
            self.tam += 1

    def removerInicio(self):
        if self.vazia():
            print("[Lista Vazia]")
            return
        else:
            removido = self.header.next
            proximo = removido.next
            self.header.next = proximo
            proximo.prev = self.header

            self.tam -= 1
        return removido

    def removerFim(self):
        if self.vazia():
            print("[Lista Vazia]")
            return
        else:
            removido = self.trailer.prev
            penultimo = removido.prev
            penultimo.next = self.trailer
            self.trailer.prev = removido.prev
            self.tam -= 1
        return removido

    def remover(self, item):
        if self.vazia():
            print("[Lista Vazia]")
            return
        else:
            busca = self.buscar(item)
            if(not busca):
                print("[Valor inexistente]")
                return
            else:
                removido = busca
                if (self.tam == 1):
                    busca.prev = busca.next
                    busca.next.prev = busca.prev.next
                else:
                    if (busca.prev != self.header or busca.next != self.trailer):
                        busca.prev.next = busca.next
                        busca.next.prev = busca.prev                
                self.tam -= 1
                
            return removido

    def substituir(self, item, novoItem):
        if self.vazia():
            print("[Lista Vazia]")
            return
        else:
            busca = self.buscar(item)
            if(not busca):
                print("[Valor inexistente]")
            else:
                busca.dado = novoItem

    def imprimir(self):
        if not self.vazia():
            item = self.header.next
            while item != self.trailer:
                print(item)
                item = item.next
                
    def buscar(self, alvo):
        if not self.vazia():
            item = self.header.next

            while item != self.trailer:
                if str(alvo) == str(item):
                    return item

                item = item.next
        else:
            print("[Lista Vazia]")
            return


  
    def sorts(self, ordem):        
        if not self.vazia():
             troca = True
             while troca:
                 troca = False
                 add = self.header.next                
                 while add != self.trailer:                      
                     if(add.prev !=self.header):
                         if(ordem =="asc"):
                             if(add.prev > add ):
                                 aux1 = add.dado
                                 aux2 = add.prev.dado
                                 self.substituir(aux1,aux2)       
                                 self.substituir(aux2,aux1) 
                                 troca = True 
                         else:
                              if(add.prev < add ):
                                 aux1 = add.dado
                                 aux2 = add.prev.dado
                                 self.substituir(aux1,aux2)       
                                 self.substituir(aux2,aux1) 
                                 troca = True 

                     add = add.next

        else:
            print("[Lista Vazia]")
            return
        pass
