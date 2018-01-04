class ImpostoÉRoubo(object):
    perc1 = 0
    perc2 = 0
    perc3 = 0
    salario = 0
    valida = False
    nome = ''
    def __init__(self):
      teste = True
      while teste == True:
        try:
          self.nome = input("\nQual é o seu nome?")
          self.salario = float(input("\nDigite o seu salário:"))
          teste = False
        except:
          print ("\nDigite apenas números no salário!")
          self.valida = True
        

    def imposto(self):
      if self.valida == True:
        pass
      else:  
        if self.salario >= 2000.01 and self.salario <= 3000:
            self.perc1 = self.salario - 2000.0
        elif self.salario >= 3000.01 and self.salario <= 4500:
            self.perc1 = 1000
            self.perc2 = self.salario - 3000.0
        elif self.salario > 4500:
            self.perc1 = 1000
            self.perc2 = 1500
            self.perc3 = self.salario - 4500.0
        else:
            print("Isento de impostos")

    def saida(self):
        a = self.perc1 * 8 / 100
        b = self.perc2 * 18 / 100
        c = self.perc3 * 28 / 100
        if self.perc1 != 0:
            total = a + b + c
            x = "%.2f" % (total)
            print("{}, você terá que pagar R$ {} de impostos".format(self.nome,x))


kb = ImpostoÉRoubo()
kb.imposto()
kb.saida()
