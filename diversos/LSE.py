class Nodo:

    def __init__(self,dado):
        self.dado = dado
        self.next = None

    def __str__(self):
        return self.dado


class LSE:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def inserirInicio(self,item):
        if self.size == 0:
            self.head = item
            self.tail = item

        else: #lista com 1 ou + elementos
            primeiro_item = self.head
            self.head = item
            item.next = primeiro_item
        self.size += 1
    def imprimir(self):
        i = self.head
        while (i!= None):
            print (i)
            i = i.next

lista = LSE()

lista.inserirInicio( Nodo("abc"))

lista.imprimir()

print()
lista.inserirInicio( Nodo("def"))
lista.imprimir()
