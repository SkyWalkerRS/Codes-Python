class Dnodo(object):
  def __init__(self,dado,anterior = None, proximo = None):
    self._dado = dado
    self._anterior = anterior
    self._proximo = proximo
    
  def getAnterior(self):
    return self._anterior
  
  def setAnterior(self,novo):
    self._anterior = novo
  
  def getProximo(self):
    return self._proximo
    
  def setProximo(self,novo):
    self._proximo = novo
    
  def getDado(self):
    return self._dado
  
  def setDado(self,novo):
    self._dado = novo
    
  def __str__(self):
    return str(self.getDado())
  

class LDE(Dnodo):
  def __init__(self,inicio = None, fim = None):
    self._inicio = inicio
    self._fim = fim
    
  
  def vazio(self):
    if self._inicio is None:
      return True
  
  
  def inserir(self,valor):
    newNodo = Dnodo(valor)
    if self.vazio() == True:
      self._inicio = newNodo
      self._fim = newNodo
    else:
      newNodo.setProximo(self._inicio)
      self._inicio.setAnterior(newNodo)
      self._inicio = newNodo
  def inserirFinal(self,valor):
    newNodo = Dnodo(valor)
    if self.vazio() == True:
      newNodo = Dnodo(valor)
      self._inicio = newNodo
      self._fim = newNodo
    else:
      self._fim.setProximo(newNodo)
      newNodo.setAnterior(self._fim)
      self._fim = newNodo
      
      
  def buscar(self,valor):
    if self.vazio() == True:
      return None
    else:
      i = self._inicio
      while i != None:
        print(i)
        if i.getDado() == valor:
          print (i)
        else:  
          i = i.getProximo()
      return None
        
    
    
  def remove(self,valor):
    x = self.buscar(valor)
    if x == None:
      return -1
    if self._inicio != self._fim:
      if x == self._inicio:
        n = self._inicio.getProximo() #n = next
        n.setAnterior(None)
        self._inicio = n
      elif x == self._fim:
        p = self._fim.getAnterior() #p = previous
        p.setProximo(None)
        self._fim = p
      else:
        p = x.getAnterior()
        n = x.getProximo()
        n.setAnteroior(p)
        p.setProximo(n)
    else:
      self._inicio = None
      self._fim = None
        

teste = LDE()
teste.inserirFinal(Dnodo('\nA'))
teste.inserirFinal(Dnodo('B'))
teste.inserirFinal(Dnodo('C'))


teste.inserir(Dnodo('A'))
teste.inserir(Dnodo('B'))
teste.inserir(Dnodo('C'))

print(teste.buscar(Dnodo))