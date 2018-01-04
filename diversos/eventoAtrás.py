ano_atual = 2017
evento = int(input("A quanto tempo atrás ocorreu o evento?"))
def anos_atras(ano_atual,evento):
  if evento <=ano_atual: 
    aconteceu = ano_atual - evento
    print (aconteceu ,"D.C")
  elif evento > ano_atual:
    aconteceu = (ano_atual - evento) *(-1) #A resposta em A.C dava em negativo,por isso eu usei o *(-1) para transformar em positivo.
    print (aconteceu,"A.C")
    
    
    
(anos_atras(ano_atual,evento))  

