import os
#def Input(retorno,type=None):
#        try:
#            if(type=="int"):
#                return int(retorno)                
#            elif(type=="float"):
#                return float(retorno)                
#            else:
#                return retorno            
#        except ValueError:
#            return False
#ret = ""
#while True:    
#    ret=Input(input("odigite aqui"),"float")
#    if(ret != False):
#        break
#print(ret)




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


class Switch:
    def __init__(self, value): 
        self._val = value

    def __enter__(self): 
        return self

    def __exit__(self, type, value, traceback): 
        return False 

    def __call__(self, cond, *mconds): 
        return self._val in (cond,)+mconds

def limpar():
    pass
    #os.system('clear')
    os.system('CLS')









