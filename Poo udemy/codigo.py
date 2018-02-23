

class Data:

    def __init__(self, dia, mes, ano ):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        print(self)

    @classmethod
    #como se fosse um construtor alternativo, onde 'cls' é a classe 'Data'
    def de_string(cls, data_string ): #10-10-2016
        dia, mes, ano = map(int, data_string.split('-')) #o map é p/ converter em inteiro a data em string e o split remove os ífens
        data = cls(dia, mes, ano)
        return data

    @staticmethod #não pode ser herdado, é apenas uma função p/ auxiliar, ex: na validação de algum método.
    def is_date_valid(data_string):
        dia, mes, ano = map(int, data_string.split('-'))
        return dia <= 31 and mes <= 12 and ano <= 2020


data = Data(10, 10, 10)        
data1 = Data.de_string("10-10-2016")
print(data1)
vdd = Data.is_date_valid("31-10-2016")
print(vdd)

