lista = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
ncasos = int( input('Informe o número de palavras a serem decodificadas: ') )
for caso in range(0,ncasos):
    palavra = input('Informe a palavra a ser decodificada: ')
    salto = int( input('Informe o número de saltos da critografia: ') )
    saida =  ""
    for letra in palavra:
        posicao = lista.index(letra) - salto
        if posicao<0:
            posicao = posicao+26
        saida = saida + lista[posicao]
    print("Palavra Decriptografada: ", saida)
