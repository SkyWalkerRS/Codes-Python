from models.tanque import *
from models.usuario import *
from dao.tanquedao import *
from dao.usuariodao import *
from factory.bancodedados import *
from pattern.conexaofactorypattern import *
from pattern.tanquedaopattern import *
from pattern.usuariodaopattern import *
from utils.tools import *
import sys




conn = ConexaoFactory().getConexao()

tanqueDao = TanqueDao(conn)
usuarioDao = UsuarioDao(conn)
os = Tools()
while True:           
        os.limpaTela()
        print("Tela de Login:")
        login = input("Login:")
        senha = input("Senha:")	
        user = usuarioDao.getListaPesquisa(1)          
        if(len(user)==0):          
           ConexaoFactory().inicializarDados(True)        
        user = usuarioDao.getLista()
        valido = False
        for item in user:
                if(item.getLogin() == login and item.getSenha() == senha):
                    valido = True;
                    break;
        if(valido):            
            user = usuarioDao.getListaPesquisa(1)
            if(user[0].getLogin() == "admin" and user[0].getSenha() == "admin"):               
                login = input("novo Login:")
                senha = input("nova Senha:")
                usuario = Usuario(1,login,senha)
                usuarioDao.saveOrUpdate(usuario,False)
            break
        else:
            input("login ou senha incorreta")



while True:

    print("*** M E N U  P R I N C I P A L ***")
    os.limpaTela()
    print("Digite:")
    print("[1] para cadastrar")
    print("[2] para alterar:")
    print("[3] para pesquisar tudo:")
    print("[4] para pesquisar por categoria:")
    print("[5] para excluir")
    print("[6] para alterar carga tanque")
    print("[7] para sair")
    escolha = input("O que deseja fazer?")
    if escolha == '1':	
        escolha2 = input("Digite:\n[1] para cadastrar um Tanque:\n[2] para cadastrar um Usuario:")
        if escolha2 == '1':
            aux = True #variavel auxiliar para definir se o usuario quer cadastrar ou alterar.. true cadastra false altera
            cor = input("Digite a cor do tanque")
            while True:
            
                capacidade = float(Input("Digite a capacidade do tanque:"))
                if capacidade == 0:
                    print("Caro usuário, vc não pode cadastrar a capacidade coomo 0")
                    input("Press (enter) para voltar ao menu")
                    break

                leite = input("Tipo do leite:\nDigite:\n[1] leite cru\n[2] leite pasteurizado\n[3] Leite Desnatado")
                if capacidade < 0:
                    capacidade = capacidade*(-1)
                if leite == '1':
                    tipo = "Cru"                
                elif leite == '2':
                    tipo = "Pasteurizado"
                elif leite == '3':
                    tipo = "Semi Desnatado"    
                tanque = Tanque(0,cor,capacidade,tipo,0)

                tanqueDao.saveOrUpdate(tanque,aux)
                print("cadastrado com sucesso")
                input("Press (enter) para voltar ao menu")
                break	
        elif escolha2 == '2':
            while True:

                login = input("Defina seu login:")
                vet = []
                for i in usuarioDao.getLista():
                    vet.append(i.login)
                if login in vet:
                    print("Login existente...")
                    input('press (Enter) para voltar ao Menu')
                    break

                else:
                    senha = input("Defina a senha:")
                    usuario = Usuario(1,login,senha)
                    usuarioDao.saveOrUpdate(usuario)
                    print("cadastrado com sucesso")
                    input('press (Enter) para voltar ao Menu')
                    break
    elif escolha == '2':        
        escolha2 = input("Digite:\n[1] para alterar um usuário\n[2] para alterar um tanque")
        if escolha2 == '1':
            x = True
            while x == True:


           
               
                cod = int(Input("Digite o código do usuário para alterar.."))
                vet = []
                for i in usuarioDao.getLista():
                    vet.append(i.cod)
                if cod not in vet:
                    print("Código inexistente")
                    input('press (Enter) para voltar ao Menu')
                    break
                else:
                    print("Digite o login e senha para confirmar a alteração:")
                    log = input("Login:")
                    senha = input("Senha:")
                    user = usuarioDao.getLista()
                    a = False
                    for i in user:
                        if(item.getLogin() == login and item.getSenha() == senha):
                            a = True
                        else:
                            a = False
                    if a == True:

                        novaSenha = input("Digite sua nova senha")
                        usuarioAlterado = Usuario(cod,login,novaSenha)
                        usuarioDao.saveOrUpdate(usuarioAlterado,False)
                        print("Usuário alterado!")
                        input('press (Enter) para voltar ao Menu')
                        break
                    elif a == False:
                        print("login ou senha erradas")
                        input("Press (enter) para voltar ao menu")
                        break
                        #else:
                            #print('Login ou senha incorretos')

                            #break
                #break


        else:
            print(''' Tanques disponíveis\n--------------------\n''')
            listaId = []
            for tanque in tanqueDao.getLista():
                print("----------------------")
                listaId.append(tanque.cod)
                print(tanque.cod,tanque.cor,tanque.capacidade,tanque.tipo,tanque.carga)

            while True:
                try:
                    cod = int(Input("Digite o código do tanque que deseja alterar:"))
                    break
                except ValueError:
                    print("Digite apenas números inteiros\n")
            if cod not in listaId:
                print("ID Inexistente")
                input("Press (enter) para voltar ao menu")
                
            else:
                carg = tanqueDao.getListaPesquisa(cod)[0].carga
                print(carg)
                aux = False # False altera algo na def
                cor = input("Digite a nova cor para o tanque:")            
                leite = input("Tipo do leite:\nDigite:\n[1] leite cru\n[2] leite pasteurizado\n[3]")
                if leite == '1':
                    tipo = "Cru"
               
                elif leite == '2':
                    tipo = "Pasteurizado"
                elif leite == '3':
                    tipo = "Semi Desnatado"               
                capacidade = float(Input("Digite a nova capacidade para o tanque:"))
                if leite == '1':
                        if(capacidade<carg):
                            print("Capacidade menor que a carga, remova a carga antes de prosseguir")
                        else:
                            novoTanque = Tanque(cod,cor,capacidade,tipo,carg)
                            tanqueDao.saveOrUpdate(novoTanque,aux)
                            print("Tanque alterado!")
                            input("Press (enter) para voltar ao menu")

               
                elif leite == '2':
                        if((capacidade-(capacidade*10)/100)<carg):
                            print("Capacidade menor que a carga, remova a carga antes de prosseguir")

                        else:
                            novoTanque = Tanque(cod,cor,capacidade,tipo,carg)
                            tanqueDao.saveOrUpdate(novoTanque,aux)
                            print("Tanque alterado!")
                            input("Press (enter) para voltar ao menu")
                elif leite == '3':
                    if((capacidade-(capacidade*5)/100)<carg):
                         print("Capacidade menor que a carga, remova a carga antes de prosseguir")
                    else:
                        novoTanque = Tanque(cod,cor,capacidade,tipo,carg)
                        tanqueDao.saveOrUpdate(novoTanque,aux)
                        print("Tanque alterado.")     



                            
            
                print("Tanque alterado..")
    elif escolha == '3':
        escolha2 = input("Digite:\n[1] para pequisar todos os Usuários:\n[2] para pesquisar todos os Tanques:")
        if escolha2 == '1':
            for i in usuarioDao.getLista():
                print("Cod:" + str(i.cod) + " Login:" + i.login + " Senha:" + i.senha)
            input("\nClique para voltar ao menu...\n")
        else:
            
            for i in tanqueDao.getLista():
                print("Cod: " + str(i.cod) + ' Cor:' + i.cor+ ' capacidade:'+ str(i.capacidade) + ' Tipo:'+ i.tipo + ' Carga: '+ str(i.carga))
            input("\nClique para voltar ao menu...\n")	

    elif escolha == '4':
        escolha2 = input("Digite:\n[1] para pequisar um Usuário:\n[2] para pesquisar um Tanque:")
        if escolha2 == '1': 
            while True:
                try:
                    cod = int(Input("Digite o código para pesquisar:"))
                    break
                except ValueError:
                    print("\nDigite apenas números!\n")
            for i in usuarioDao.getListaPesquisa(cod):
                print(i)
        else:
            print("Digite para Pesquisar por:\n[1] Código:\n[2] Cor:\n[3] Capacidade:\n[4] Tipo:\n")
            opcao = int(Input("O que deseja fazer?"))
            tipes = ["COD","COR","CAPACIDADE","TIPO"]
            while True:
                try:
                    if opcao == 1:
                        value = int(Input("Digite o código para pesquisar:"))
                    elif opcao == 2:	
                        value = input("Digite a cor para pesquisar:")
                    elif opcao == 3:	
                        value = float(Input("Digite a Capacidade para pesquisar:"))
                    elif opcao == 4:	
                        value = input("Digite a Tipo para pesquisar:")		
                    break
                except ValueError:
                        print("\nDigite apenas números!\n")
            for i in tanqueDao.getTanque(tipes[opcao-1],value):
                print(i)		


    elif escolha == '5':
        escolha2 = input("Digite:\n[1] para excluir um Usuário:\n[2] para excluir um Tanque:")
        if escolha2 == '1':
            usuarioDao.excluir(int(Input("Digite o código do usuário para deletar:")))
            print("Usuário deletado")

            input("Press (enter) para voltar ao menu")

                    
        else:
            while True:
                try:
                    cod = int(Input("Digite o código do tanque para deletar:"))
                    break
                except ValueError:
                    print("\nDigite apenas números!\n")
            tanqueDao.excluir(cod)

    elif escolha == '6':
        escolha2 = input("Digite:\n[1] para depositar uma carga:\n[2] para retirar uma carga:")
        tanque = int(Input("Qual é o codigo do tanque?"))
        

            

        if escolha2 == '1':
            deposito = float(Input("qual será o valor depositado:"))
            if(deposito<0):
                deposito = deposito*-1
            resultado =  tanqueDao.setCarga(tanque,deposito)                    
        else:
            retirada =float(Input("qual será o valor retirado:"))
            if(retirada<0):
                retirada = retirada*-1
            resultado = tanqueDao.getCarga(tanque,retirada)
    elif escolha == '7':
        print("Saindo....")
        sys.exit()
      
     
    
    

















