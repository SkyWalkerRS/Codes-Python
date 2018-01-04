lista = []
num = int(input("Digite o número da sequência:"))
while num!=-1:
  lista.append(num)
  num = int(input("Digite o número da sequência:"))
elemento = int(input("Qual o elemento vc quer contar?"))
n = 0
for i in range(len(lista)):
  if lista[i] == elemento:
    n +=1
print ("O elemento %i aparece %i vezes"%(elemento,n))

  
  
  