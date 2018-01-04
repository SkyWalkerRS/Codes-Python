import sys
class Voo(object):
  listaVoo = []
  def __init__(self,numero,origem,destino,lugares):
    self.numero = numero
    self.origem = origem
    self.destino = destino
    self.lugares = lugares
   
    
    
  def __str__(self):
    return "                                                                                                                                                                        Número do Vôo : " + str(self.numero) + "                                                                                                                                                                                                                                                                                                                                        "+ " Origem : " + str(self.origem) + "                                                                                                                                                                                                                                                                                                                                                     "+ " Destino : " + str(self.destino) + "                                                                                                                                                                                                                                                                                                                                                   " + " Lugares disponiveis : " +  str(self.lugares) + "                                         "                                                                                                                                        

  
  
  def criarVoo(self,voo):
    if(self.consultaNum(voo.numero) ==None):
     self.listaVoo.append(voo)
     return "cadastrado com sucesso"
    else:
        return "Voo ja cadastrado"
  
  
  def consultaNum (self,numero):  
    for num in self.listaVoo:
      if num.numero == numero:
        return (num) 
         
    
        
  
  
  def consultaOrigem(self,origem):
    retorno = []
   
    for i in self.listaVoo:
      if i.origem == origem:
        retorno.append(str(i))

    if(len(retorno)==0):
        return("Vôo inexistente") 
    else:
        return (str(retorno).strip('[]')) 
       
  
  
  
  def consultaDestino(self,destino):
    retorno = []
    for dest in self.listaVoo:
      if dest.destino == destino:
        retorno.append(str(dest))

    if(len(retorno)==0):
        return("Vôo inexistente") 
    else:
        return (str(retorno).strip('[]')) 
        
        
        
  
    
  def efetuarReserva (self,numero):
    busc = self.consultaNum(numero)
    if(busc !=None):
        if busc.lugares > 0:
          busc.lugares -= 1
          return "Reserva Confirmada"
    
        else:
          return "Poltrona reservada. Aguardando liberação da companhia."
    else:
        return "Vôo inexistente"
  def menu(self):
    return "Número de voos cadastrados:" + str(len(self.listaVoo))
    
  def menu2(self):
    x = []
    for i in self.listaVoo:
      x.append(i.lugares)
    return sum(x)  
      
  def menu3(self):
    listaTodos = []
    for i in self.listaVoo:
      listaTodos.append(str(i))
    return listaTodos  
    
    
while True:
  try:
     menu = int(input("\n\n** Menu Principal **\n\nDigite: \n\n1 para cadastrar um voo\n\n2 para consultar\n\n3 para efetuar reserva\n\n4 para sair\n\n5 para um menu adicional:"))
     if menu == 1:
       try:
         numero = int(input("Defina o número do voo:"))
         origem = input("Defina a origem:")
         destino = input("Defina o destino:")
         lugares = int(input("Defina os lugares:"))
         voo = Voo(numero,origem,destino,lugares)
         print(voo.criarVoo(voo))
       except ValueError:
         print("Digite apenas números!!!")
       
     elif menu == 2:
       try:
         m2 = int(input("\n\nComo deseja consultar seu voo?\n1: Por número de voo\n2: Por origem\n3: Por destino\n"))
         if m2 == 1:
           print(voo.consultaNum(int(input("Informe o numero para busca:"))))
         elif m2 == 2:
          print(voo.consultaOrigem(input("Informe a origem para busca:")))
         elif m2 == 3:
          print(voo.consultaDestino(input("Informe o destino para busca:")))
       except ValueError:
        print("Digite apenas números inteiros!")
      
     elif menu == 3:
      print(voo.efetuarReserva(int(input("Digite o número para reservar o Voo:"))))
  
  
     elif menu == 4:
       print("\n\nVolte quando quiser !!")
       sys.exit()
     elif menu == 5:
       m = input("Digite\n\n1 para ver o Número de voos cadastrados:\n2 para ver os número de poltronas disponiveis\n3 para ver a lista de voo com as informações")
       if m == '1':
         print(voo.menu())
       elif m =='2':
        print(voo.menu2())
       elif m == '3':
         print(voo.menu3())
     else:
       print("\n\nDigite de 1 a 4")
    
  except NameError:
    print("Você não pode consultar ou reservar Vôo sem ao menos ter criado um !")
  except ValueError:
    print("\n\nO Menu do Aeroporto aceita apenas números inteiros... Caro usuário, digite novamente!\n\n")
  



