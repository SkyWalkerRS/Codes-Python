## Programa que simula um calendario
# http://pt.wikipedia.org/wiki/Calend%C3%A1rio_gregoriano
#
# Dada uma data (dia, mes, ano) por parametro e retorna o dia da semana

# Implementação de referencia: http://www.calculatorcat.com/free_calculators/day_of_week.phtml

class Calendario:
    dias_semana = (
        'Domingo',
        'Segunda-feira',
        'Terça-feira',
        'Quarta-feira',
        'Quinta-feira',
        'Sexta-feira',
        'Sábado',
    )
    
    # qtde de dias em cada mês
    mes_dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Na data 01/01/1900, o dia da semana era segunda-feira

    def __init__(self):
        print("== CALENDARIO - EDD ==")

    def isBissexto(self, ano):
        ano = float(ano)
        # Implementar o algoritmo para ano bissexto
        #    Se o ano foi divisível por quatro é preciso verificar
        #    se ele termina em 00 (zero duplo) pois ele terá que
        #    ser dividido por 400, se for, ele é bissexto,
        #    caso contrário, não.
        
        if (ano % 4 == 0.0):
            ano_str = list(str(ano)) # transforma de int para str e quebra em caracteres
            if (ano_str[2] == '0' and ano_str[3] == '0'):
                if ((ano % 400) != 0.0):
                    return False
            return True
        return False
        
    def diaDaSemana(self, data):
        # extrai dados da tupla
        dia = data[0]
        mes = data[1]
        ano = data[2]

        ano_inicial = 1900
        total_dias = 0
        while (ano_inicial <= ano):            
            if (self.isBissexto(ano_inicial) is True):
                # 'Ano Bissexto'
                self.mes_dias[1] = 29
            else:
                # 'Ano Normal'
                self.mes_dias[1] = 28
            
            # Calcula primeiro os dias corridos no ano do parametro
            dias = 0
            if (ano_inicial == ano):                
                # calcula os dias dos meses anteriores ao que foi passado
                for i in range(0,mes-1,1):                
                    dias = dias + self.mes_dias[i]

                # inclui os dias passados, subtraindo do total de dias do mes    
                dias = dias + dia
            else:
                for i in range(0, 12, 1):                    
                    dias = dias + self.mes_dias[i]

            total_dias = total_dias + dias
            
            ano_inicial += 1 # incrementa a variavel ano_inicial
        
        return self.dias_semana[total_dias % 7] # Usa o módulo para determinar o dia da semana

###############################################        
# Executando o programa
###############################################        
cal = Calendario() # instancia novo objeto
while True:
    dia = int(input('Digite o dia [dd]:'))
    mes = int(input('Digite o mês [mm]:'))
    ano = int(input('Digite o ano [aaaa]:'))
    data = (dia, mes, ano)  # tupla representando uma data

    # Para formatacoes em strings: https://mkaz.com/2012/10/10/python-string-format/    
    print('O dia da semana na data {0:0>2d}/{1:0>2d}/{2:0>4d}'.format(data[0], data[1], data[2]), 'é:', cal.diaDaSemana(data))

    opcao = input('Deseja consultar mais uma data [s/n] (padrão: n)?')
    if (opcao not in ['s','S']):
        break

