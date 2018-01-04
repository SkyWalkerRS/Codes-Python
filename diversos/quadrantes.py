x= float (input("Valor de x:"))
y= float (input("Valor de y:"))
q1 = (x> 0) and (y>0)
q2 = (x<0) and (y>0)
q3 = (x<0)and (y<0)
q4 = (x>0) and (y<0)
if (x == 0) and (y==0):
  print ("Origem")
elif x ==0:
  print ("Eixo X")
elif y==0:
  print ("Eixo y")
elif q1:
  print("1º Quadrante")
elif q2:
  print ("2º Quadrante")
elif q3:
  print ("3º Quadrante")
elif q4:
  print ("4º Quadrante")