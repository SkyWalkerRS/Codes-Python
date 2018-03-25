# decimal para binario usando pilha
class Pilha:
    lista = []

    def push(self, item):
        self.lista.append(item)
    
    def pop(self):
        return self.lista.pop()

    def peek(self):
        # retorna o ultimo item da lista, sem remover
        return self.lista[-1]

    def is_empty(self):
        if len(self.lista) > 0:
            return False
        return True

    def size(self):
        return len(self.lista)

    def __str__(self):
        return str(self.lista).strip('[]') ## retorna uma lista como string sep. por virgula

'''
p = Pilha()
p.push(1)
p.push(0)
print(p)    
'''
p = Pilha()
valor = int(input("Digite um valor decimal: "))


resultado = valor
while resultado > 0:
    (resultado, resto) = divmod(resultado,2)
    p.push(resto)

binario = []
while not p.is_empty():
    binario.append(p.pop())

print(binario)






