#Distância entre dois pontos
import math

def calcula():
    while True:
        x1 = float(input("Digite o valor de X1:"))
        y1 = float(input("Digite o valor de Y1:"))
        x2 = float(input("Digite o valor de X2:"))
        y2 = float(input("Digite o valor de Y2:"))

        d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        print("Aproximadamente:{0:.2f} u.c".format(d))
        escolha = input("\nDeseja continuar? [S/N]")
        if escolha == 's' or escolha == 'S':
            pass
        else:
            break


calcula()
