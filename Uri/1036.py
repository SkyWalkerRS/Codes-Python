#Fórmula de Bháskara
import math
def calcula():

    a = float(input("Digite o valor de a:"))
    b = float(input("Digite o valor de b:"))
    c = float(input("Digite o valor de c:"))
    delta = (b**2) - 4*a*c
    if delta <0:
        print("Impossível calcular raiz negativa")
        calcula()

    else:
        u = math.sqrt(delta)
        x1 = (b + u) /2 * a
        x2 = (b - u) /2 * a
        print("x2 = ",x2)
        print("x1 = ",x1)
        opcao = input("Deseja calcular mais? [S/N]")

        if opcao == "s" or  opcao == "S":
            calcula()




calcula()
