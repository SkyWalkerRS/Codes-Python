import os
class Tools(object):


	def limpaTela(self):
		os.system('cls'if os.name == 'nt'else 'clear')

class Input(object):
    def __init__(self, text):       
        self.text = text        

    def __str__(self):
        return input(str(self.text))
        
    def __float__(self):
         while True:
             try:
                  return float(input(str(self.text)))       
             except ValueError:
                 print("Esse Valor não é um numero com virgula")
       
    def __int__(self):
         while True:
             try:
                  return int(input(str(self.text)))       
             except ValueError:
                 print("Esse Valor não é um numero inteiro")