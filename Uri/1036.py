#Fórmula de Bháskara
import math
def errado():
    while True:
        print("Bem vindo ao resolvedor de Bháskara !!!")


        try:
            a = float(input("Digite o valor de a:"))
            b = float(input("Digite o valor de b:"))
            c = float(input("Digite o valor de c:"))
            u = math.sqrt(b *b - 4 *a *c)

            x1 = (b + u) /2 * a
            x2 = (b - u) /2 * a
            print("x2 = ",x2)
            print("x1 = ",x1)
            print("Se deseja sair digite 's' or 'S':\nOutra tecla para continuar")
            opcao = input()
            if opcao == "s" or  opcao == "S":
                break

        except ValueError:
            print("Valores incorretetos")
            print("Se deseja sair digite 's' or 'S':\nOutra tecla para continuar")
            opcao = input()
            if opcao == "s" or  opcao == "S":
                break

errado()
