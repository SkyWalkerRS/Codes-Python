idade = int(input("Digite sua idade em dias"))
ano = idade//365
mes = (idade - (ano*365))//30
dia = (idade -(ano*365) - (mes*30))
print (ano,"ano(s)")
print (mes,"mes(es)")
print (dia,"dia(s)")
