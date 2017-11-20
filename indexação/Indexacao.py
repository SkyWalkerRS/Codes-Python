
import glob, os, codecs, sys
class Termo:
   
    def __init__(self):
        self.termo=""
        self.docs=[]
    def __str__(self):
        # { 'Termo" : [doc1.txt, doc2.txt, ...] }
        retorno =""
        for item in range(len(self.docs)):
            if(item != 0):
                retorno=retorno+","
            retorno =retorno+self.docs[item]
        return "'{0}':[{1}]".format(self.termo,retorno)

class Index():
    def __init__(self):
        self.Stopwords()
        self.listaIndexada=[]        
        
    def add_doc(self, nome_arquivo, conteudo_documento): 
        arquivo = open("docs/"+nome_arquivo + '.txt', 'a')
        arquivo.write(conteudo_documento + "\n")
        arquivo.close()

    def excluir_entradas_doc(self,nome_arquivo): 
        repetido = True
        while (repetido):
            repetido = False
            for palavrasObj in self.listaIndexada:
                for doc in palavrasObj.docs:
                    if(doc == nome_arquivo):
                        palavrasObj.docs.remove(doc)
                        repetido = True
                        break
                if(len(palavrasObj.docs)==0):
                    repetido = True
                    self.listaIndexada.remove(palavrasObj)

           

    def buscar(self,arg):
        buscaAnd=False
        if("AND" in arg):
            buscaAnd = True
            arg = arg.replace(" AND",'')
            arg = arg.replace("AND",'')
        if("OR" in arg):
            buscaAnd = False
            arg = arg.replace(" OR",'')
            arg = arg.replace("OR",'')
        listaArg= arg.split(" ")  
        resultado =[]
        for palavrasObj in self.listaIndexada: 
            for busca in listaArg:                
                if(palavrasObj.termo == busca):
                    resultado = resultado + palavrasObj.docs
        if(buscaAnd):             
          resultado = [item for item in set(resultado) if resultado.count(item) > 1]          
        print("O resultado da buscas é :")               
        if(len(resultado)==1): 
            print(1,"Documento")
        if(len(resultado)>1): 
            print(len(resultado),"Documentos")   
        if(len(resultado)==0):
            print("Sem resultado")   
        else:
            for item in resultado:            
                print(item)       

    
    def Stopwords(self):
        self.stopwords = []
        arquivos = 'stopwords.txt'
        f = codecs.open(arquivos, "r",)
        linhas = f.readlines()
        for linha in linhas:
            self.stopwords.append(linha.replace('\n', '').strip())
        f.close()


    def Mostrarindex(self):
        for palavrasObj in self.listaIndexada: 
            print(palavrasObj)
        print("total:",len(self.listaIndexada))
        

    def Indexar(self):
      self.listaIndexada=[]
      for i, arq in enumerate(glob.glob("docs/*.txt")):        
        # Abrir arquivo
        f = codecs.open(arq, "r")
        arq = arq.replace('docs\\', '')
        arq = arq.replace('docs/', '')

        linhas = f.readlines()
        for i, linha in enumerate(linhas):
            linha = linha.lower()         
            linha =linha.replace('\n', '')
            for removerChars in ["(", ")", "[", "]","{","}" ,'"',"'",",", "."]:
                linha = linha.replace(removerChars, "")
            listaTokens = linha.split(" ")
            for token in listaTokens:                  
                for remover in  self.stopwords:
                    if(token==remover):
                        listaTokens.remove(token)
                        break
            for token in listaTokens:
                
                nova = True
                for palavrasIndex in self.listaIndexada:
                    if(palavrasIndex.termo==token):
                        novoDoc = True
                        for doc in palavrasIndex.docs:                            
                            if doc == arq:
                                novoDoc=False;
                                break
                        if(novoDoc):
                            palavrasIndex.docs.append(arq)     
                                                      
                        nova = False                        
                        break
                if nova:
                    NovaPalavraObj = Termo()
                    NovaPalavraObj.docs.append(arq)
                    NovaPalavraObj.termo = token
                    self.listaIndexada.append(NovaPalavraObj)
        


                

             
        
######################################################################################################33333
index = Index()
a = False
while True:
    print('''1.Adicionar Documento Manualmente
2.Remover Documento
3.Indexar documentos '.txt' presentes na pasta docs
4.Buscar termos
5.Mostrar Índice Invertido''')
    opcao = input("O que deseja fazer?")
    if opcao == '1':
        nome = input("Digite o nome do documento:")
        conteudo = input("Digite no documento:")
        index.add_doc(nome,conteudo)
        print("Documento adicionado com sucesso!")
        input("Clique para voltar ao menu")
    elif opcao == '2':
        if a == False:
            print("Você precisa indexar para realizar este procedimento!")
            input("Clique para voltar ao Menu")

        else:
            nome = input("Digite o nome do arquivo deletar o algum conteúdo:")
            index.excluir_entradas_doc(nome)
    elif opcao == '3':
        print("Indexado com sucesso!!")
        a = True
        index.Indexar()
        input("Clique para voltar ao menu..")
       
    elif opcao == '4':
        if a == False:
            print("Você precisa indexar para realizar este procedimento!")
            input("Clique para voltar ao Menu")
        else:

            index.buscar(input("Digite o valor que deseja pesquisar:"))

        
    elif opcao == '5':
        if a == False:
            print("Você precisa indexar para realizar este procedimento!")
            input("Clique para voltar ao Menu")
        else:
            print(index.Mostrarindex())


       
       
            

