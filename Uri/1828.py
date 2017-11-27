#The Big Bang Theory
#Pedra papel tesoura lagarto Spock
class PedraPapelTesouraLagartoSpock():
    def __init__(self):
        self.raj = ''
        self.sheldon = ''
        self.caso = 1

    def bazinga(self,casos):

        for i in range(0,casos):
            self.sheldon = input("Sheldon joga: ")
            self.raj = input("Raj joga: ")

            self.ganhador()
            self.caso +=1
    def ganhador(self):
        j1 = self.sheldon.upper()
        j2 = self.raj.upper()
        if j2 == j1:
            print("Caso #{} de novo!!".format(self.caso))
        elif j1 == "TESOURA":
             if j2 == "PAPEL" or j2 == "LAGARTO":
                 print("Caso #{} Bazinga!!".format(self.caso))
             elif j2 == "SPOCK" or j2 == "PEDRA":
                 print("Caso #{} Raj trapaceou".format(self.caso))
        elif j1 == "PEDRA":
             if j2 == "LAGARTO" or j2 == "TESOURA":
                print("Caso #{} Bazinga!!".format(self.caso))
             elif j2 == "SPOCK" or j2 == "PAPEL":
                print("Caso #{} Raj trapaceou".format(self.caso))
        elif j1 == "SPOCK":
            if j2 == "TESOURA" or j2 == "PEDRA":
                print("Caso #{} Bazinga!!".format(self.caso))
            elif j2 == "PAPEL" or j2 == "LAGARTO":
                print("Caso #{} Raj trapaceou".format(self.caso))
        elif j1 == "LAGARTO":
            if j2 == "PAPEL" or j2 == "SPOCK":
                print("Caso #{} Bazinga!!".format(self.caso))
            elif j2 == "PEDRA" or j2 == "TESOURA":
                print("Caso #{} Raj trapaceou".format(self.caso))
        elif j1 == "PAPEL":
            if j2 == "PEDRA" or j2 == "SPOCK":
                print("Caso #{} Bazinga!!".format(self.caso))
            elif j2 == "LAGARTO" or j2 == "TESOURA":
                print("Caso #{} Raj trapaceou".format(self.caso))

print("Bem vindo ao jogo Pedra Papel Tesoura Lagarto Spock!!")
casos_teste = int(input("\nQuantas vezes quer jogar?"))


jogar = PedraPapelTesouraLagartoSpock()
jogar.bazinga(casos_teste)
