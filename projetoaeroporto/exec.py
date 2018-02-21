from models.Aeroporto import Aeroporto
from models.Voo import Voo
from models.Passageiro import Passageiro
from factory.conexaoFactory import ConexaoFabrica
from dao.aeroportoDao import AeroportoDao
from dao.passageiroDao import PassageiroDao
from dao.vooDao import VooDao
import os
import sys

from tools.utilidades import Tam




p = Tam()


conn = ConexaoFabrica().getConexao()
vooDao = VooDao(conn)
aeroportoDao = AeroportoDao(conn)
passageiroDao = PassageiroDao(conn)


#Definindo as listas para pesquisa.


listaAeroporto = aeroportoDao.listar()
listaPassageiros = passageiroDao.listar()


while True:
	while True:
		os.system('clear')
		print("*** M E N U  P R I N C I P A L ***")
		print("Digite:")
		print("(1) para cadastrar no banco de dados:")
		print("(2) para alterar algo") 
		print("(3) para deletar")
		print("(4) para pesquisar no banco de dados")
		print("(5) para pesquisar por id")
		print("(6) para pesquisar por outras informações:")
		print("(7) para sair")
		escolha = input("O que deseja fazer?")
		if escolha == '1':
			print("** S U B  -  M E N U **")
			print("Digite:")
			print("(1) para cadastrar um Voo: ")
			print("(2) para cadastrar um Aeroporto: ")
			print("(3) para cadastrar um Passageiro: ")
			
			escolha2 = input("O que deseja fazer?")
			if escolha2 == '1':
				numero = input("Defina o número do Voo:")
				if len(numero) == 0:
					p.semTexto()
					break
				aux = []
				for voo in vooDao.listar():
					aux.append(voo.numero)
				if numero in aux:
					print("Não foi possível cadastrar\nJá existe um voo com este número")
				else:
						

					origem = input("Defina a origem do Voo:")
					if len(origem) == 0:
						p.semTexto()
						break
					destino = input("Defina o destino do Voo:")
					if len(destino) == 0:
						p.semTexto()
						break
					while True:
						try:
							lugares = int(input("Defina o número de lugares do Voo:"))
							if lugares == 0:
								lugares = 15
							break
						except ValueError:
							print("Digite apenas números\n")

						
					voo = Voo(0,numero,origem,destino,lugares)
					vooDao.cadastrar(voo)
					print("Voo cadastrado")
					input('\n...\n')
			elif escolha2 =='2':
				nome = input("Defina o nome do aeroporto:")
				if len(nome) == 0:
					p.semTexto()
					break
				sigla = input("Defina a sigla:")
				if len(sigla) == 0:
					p.semTexto()
					break
				aeroporto = Aeroporto(0,nome,sigla)
				aeroportoDao.cadastrar(aeroporto)
				print("Aeroporto cadastrado!!")
				input('\n...\n')
			elif escolha2 == '3':
				nome = input("Digite o nome do passageiro:")
				if len(nome) == 0:
					p.semTexto()
					break
				cpf = input("Digite o CPF:")
				if len(cpf) == 0:
					p.semTexto()
					break
				vet = []
				for i in passageiroDao.listar():
					vet.append(i.cpf)
				if cpf in vet:
					print("Erro\nNão pode haver 2 cpfs iguais")
					input("\n...\n")
				else:		


					while True:
						try:
							idade = int(input("Digite a idade:"))
							break
						except ValueError:
							print("Digite apenas números\n")
						
					passageiro = Passageiro(0,nome,cpf,idade)
					passageiroDao.cadastrar(passageiro)
					print("Passageiro cadastrado!!")
					input('\n...\n')
		elif escolha == '2':
			print("** S U B  -  M E N U **")
			print("Digite:")
			print("(1) para alterar um Voo: ")
			print("(2) para alterar um Aeroporto: ")
			print("(3) para alterar um Passageiro: ")
			escolha2 = input("O que você deseja fazer?")
			if escolha2 == '1':
				print("Todos os voos:")
				print("--------------------------------------------------")
				for voo in vooDao.listar():
					print(voo.iden,voo.numero,voo.origem,voo.destino,voo.lugares)
				print("--------------------------------------------------")
				while True:
					try:
						mudar = int(input("Digite o id do voo que deseja alterar"))
						break
					except ValueError:
						print("Digite apenas inteiros")
				numero = input("Defina o número do Voo:")
				if len(numero) == 0:
					p.semTexto()
					break

				origem = input("Defina a origem do Voo:")
				if len(origem) == 0:
					p.semTexto()
					break
				destino = input("Defina o destino do Voo:")
				if len(destino) == 0:
					p.semTexto()
					break
				while True:
					try:
						lugares = int(input("Defina o número de lugares do Voo:"))
						if lugares == 0:
							lugares = 15
						break
					except ValueError:
						print("Digite apenas números\n")
				novoVoo = Voo(mudar,numero,origem,destino,lugares)
				vooDao.alterar(novoVoo)
				print("Voo alterado!")
				input('\n...\n')
			elif escolha2 == '2':
				print("Todos os Aeroportos:")
				print("--------------------------------------------------")
				for aero in aeroportoDao.listar():
					print(aero.iden,aero.nome,aero.sigla)
				print("--------------------------------------------------")
				while True:
					try:
						mudar = int(input("Digite o id do aeroporto que deseja alterar"))
						break
					except ValueError:
						print("Digite apenas inteiros")
				nome = input("Defina o novo nome do aeroporto:")
				if len(nome) == 0:
					p.semTexto()
					break
				sigla = input("Defina a nova sigla:")
				if len(sigla) == 0:
					p.semTexto()
					break
				novoAero = Aeroporto(mudar,nome,sigla)
				aeroportoDao.alterar(novoAero)
				print("Aeroporto alterado!!")
				input('\n...\n')
			elif escolha2 == '3':
				print("Todos os passageiros:")
				print("--------------------------------------------------")
				for pessoa in passageiroDao.listar():
					print(pessoa.iden,pessoa.nome,pessoa.cpf,pessoa.idade)
				print("--------------------------------------------------")
				while True:
					try:
						mudar = int(input("Digite o id do passageiro que deseja alterar"))
						break
					except ValueError:
						print("Digite apenas inteiros")
				nome = input("Defina o novo nome do passageiro:")
				if len(nome) == 0:
					p.semTexto()
					break


				cpf = input("Digite o CPF:")
				if len(cpf) == 0:
					p.semTexto()
					break
				vet = []
				for i in passageiroDao.listar():
					vet.append(i.cpf)
				if cpf in vet:
					print("Erro\nNão pode haver 2 cpfs iguais")
					input("\n...\n")
				else:		


					while True:
						try:
							idade = int(input("Digite a idade:"))
							break
						except ValueError:
							print("Digite apenas números\n")
						
					passageiro = Passageiro(0,nome,cpf,idade)
					passageiroDao.cadastrar(passageiro)
					print("Passageiro cadastrado!!")
					input('\n...\n')


		elif escolha == '3':
			print("Digite:")
			print("(1) para deletar Voos:")
			print("(2) para deletar Aeroportos:")
			print("(3) para deletar Passageiros:")
			escolha2 = input("Qual deseja deletar?")
			if escolha2 == '1':
				excluir = input("Digite:\n(1) para excluir um voo por ID\n(2) para excluir todos os Voos cadastrados.")
				if excluir == '1':
					while True:
						try:
							deleta = int(input("Digite o id do voo que deseja excluir:"))
							break
						except ValueError:
							print("Digite apenas números no campo ID")
					vooDao.excluir(deleta)
					print("Voo excluído com sucesso!")
					input('\n...\n')
				elif excluir == '2':
					x = input("VOCÊ TEM CERTEZA QUE DESEJA EXCLUIR TODOS OS VOOS CADASTRADOS? S/N")
					if x.lower() == 's':
						vooDao.deletarTudo()
						print("\nVoos deletados!")
						input('\n...\n')
			elif escolha2 == '2':
				excluir = input("Digite:\n(1) para excluir um aeroporto por ID\n(2) para excluir todos os Aeroportos cadastrados.")
				if excluir == '1':
					while True:
						try:
							deleta = int(input("Digite o id do aeroporto que deseja excluir:"))
							break
						except ValueError:
							print("Digite apenas números no campo ID")
					aeroportoDao.excluir(deleta)
					print("Aeroporto excluído com sucesso!")
					input('\n...\n')
				elif excluir == '2':
					x = input("VOCÊ TEM CERTEZA QUE DESEJA EXCLUIR TODOS OS AEROPORTOS CADASTRADOS? S/N")
					if x.lower() == 's':
						aeroportoDao.deletarTudo()
						print("\nAeroportos deletados!")
						input('\n...\n')
			elif escolha2 == '3':
				excluir = input("Digite:\n(1) para excluir um passageiro por ID\n(2) para excluir todos os Passageiros cadastrados.")
				if excluir == '1':
					while True:
						try:
							deleta = int(input("Digite o id do passageiro que deseja excluir:"))
							break
						except ValueError:
							print("Digite apenas números no campo ID")
					passageiroDao.excluir(deleta)
					print("Passageiro excluído com sucesso!")
					input('\n...\n')
				elif excluir == '2':
					x = input("VOCÊ TEM CERTEZA QUE DESEJA EXCLUIR TODOS OS PASSAGEIROS CADASTRADOS? S/N")
					if x.lower() == 's':
						passageiroDao.deletarTudo()
						print("\nPassageiros deletados!")
						input('\n...\n')					

		



		elif escolha == '4':
			print("Digite:")
			print("(1) para pesquisar todos os Voos:")
			print("(2) para pesquisar todos os Aeroportos:")
			print("(3) para pesquisar todos os Passageiros:")
			escolha2 = input("Qual deseja pesquisar?")
			if escolha2 == '1':
				for voo in vooDao.listar():
					print(voo.iden,voo.numero,voo.origem,voo.destino,voo.lugares)
				input("\nClique para voltar ao Menu!!")		
			elif escolha2 == '2':
				for aero in aeroportoDao.listar():
					print(aero.iden,aero.nome,aero.sigla)
				input("\nClique para voltar ao Menu!!")			
			elif escolha2 == '3':
				for pessoa in passageiroDao.listar():
					print(pessoa.iden,pessoa.nome,pessoa.cpf,pessoa.idade)
				input("\nClique para voltar ao Menu!!")					
		elif escolha == '5':
			print("Digite:")
			print("(1) para pesquisar um Voo:")
			print("(2) para pesquisar um Aeroporto:")
			print("(3) para pesquisar um Passageiro:")
			escolha2 = input("O que deseja pesquisar?")
			if escolha2 == '1':
				while True:
					try:
						pesquisaId = int(input("Digite o id do voo:"))
						break
					except ValueError:
						print("Digite apenas números inteiros!")
				a1 = []
				for voo in(vooDao.getId(pesquisaId)):
					print(voo)
					a1.append(voo)
				if len(a1) == 0:
					print("voo não encontrado")
				input("\nClique para voltar ao Menu!!")		
			elif escolha2 == '2':
				while True:
					try:
						pesquisaId = int(input("Digite o id do aeroporto"))
						break
					except ValueError:
						print("Digite apenas números")
				a2 = [] 		
				for aero in (aeroportoDao.getId(pesquisaId)):
					print(aero)
					a2.append(aero)
				if len(a2) == 0:
					print("Aeroporto não encontrado!!")
				input("\nClique para voltar ao Menu!!")			
			elif escolha2 == '3':
				while True:
					try:
						pesquisaId = int(input("Digite o id do passageiro:"))
						break
					except ValueError:
						print("Digite apenas números")
				a3 = []		
				for pessoa in (passageiroDao.getId(pesquisaId)):
					print(pessoa)
					a3.append(pessoa)
				if len(a3) == 0:
					print("Passageiro não encontrado!!")
				input("\nClique para voltar ao Menu!!")			
		elif escolha == '6':
			print("** S U B  -  M E N U **")
			print("Digite:")
			print("(1) para pesquisar um Voo: ")
			print("(2) para efetuar uma reserva num Voo")
			print("(3) para pesquisar um Aeroporto: ")
			print("(4) para pequisar um Passageiro: ")
			escolha2 = input("O que deseja fazer?")
			if escolha2 == '1':
				print("Digite:")
				print("(1) para pequisar por número de Voo: ")
				print("(2) para pequisar por origem de Voo: ")
				print("(3) para pequisar por destino de Voo: ")
				print("(4) para pequisar por lugares de Voo: ")
				escolha3 = input("O que quer fazer?")
				if escolha3 == '1':
					a4 = []
					numero = input("Digite o número do voo:")
					for voo in (vooDao.getNum(numero)):
						print(voo)
						a4.append(voo)
					if len(a4) == 0:
						print("Voo não encontrado!!")
					input("\nClique para voltar ao Menu!!")			
				elif escolha3 == '2':
					a5 = []
					origem = input("Digite a origem do voo:")
					for voo in (vooDao.getOrigem(origem.capitalize())):
						print(voo)
						a5.append(voo)
					if len(a5) == 0:
						print("Voo não encontrado!!")
					input("\nClique para voltar ao Menu!!")	
				elif escolha3 == '3':
					a6 = []
					destino = input("Digite o destino:")
					for voo in (vooDao.getDestino(destino.capitalize())):
						print(voo)
						a6.append(voo)
					if len(a6) == 0:
						print("Voo não encontrado!!")
					input("\nClique para voltar ao Menu!!")	
				elif escolha3 == '4':
					while True:
						try:
							lugares = int(input("Digite os lugares para pesquisa:"))
							break
						except ValueError:
							print("Informe apenas inteiros")
					a7 = []		
					for voo in (vooDao.getLugares(lugares)):
						print(voo)
						a7.append(voo)
					if len(a7) == 0:
						print("Voo não encontrado!!")
					input("\nClique para voltar ao Menu!!")	
			elif escolha2 == '2':
				numero = input("Digite o número de voo que deseja efetuar reserva:")
				u = (vooDao.efetuarReserva(numero))
				
				if u == None:
					print("VOO N EXIDSADSAKJDSKLAD")
				else:
					print(u)	

				input("\n..\n")
				break
						
			elif escolha2 == '3':
				print("Digite:")
				print("(1) para pequisar por nome: ")
				print("(2) para pequisar por sigla: ")
				escolha3 = input("O que deseja fazer?")
				if escolha3 == '1':
					nome = input("Digite o nome que deseja procurar:")
					if len(nome) == 0:
						p.semTexto()
						break
					else:
						a8 = []	
						for aeroporto in (aeroportoDao.getNome(nome.capitalize())):
							print(aeroporto)
							a8.append(aeroporto)
						if len(a8) == 0:
							print("Aeroporto não encontrado!!")
					input("\nClique para voltar ao Menu!!")	
				elif escolha3 == '2':
					sigla = input("Digite a sigla para pesquisa:")
					if len(sigla) == 0:
						p.semTexto()
						break
					else:
						a9 = []	
						for aeroporto in (aeroportoDao.getSigla(sigla.upper())):
							print(aeroporto)
							a9.append(aeroporto)
						if len(a9) == 0:
							print("Aeroporto não encontrado!!")
					input("\nClique para voltar ao Menu!!")	
			elif escolha2 == '4':
				print("Digite:")
				print("(1) para pequisar pelo Nome: ")
				print("(2) para pequisar pelo CPF: ")
				print("(3) para pequisar pela Idade: ")	
				escolha3 = input("O que deseja fazer?")
				if escolha3 == '1':
					nome = input("Digite o nome:")
					if len(nome) == 0:
						p.semTexto()
						break
					else:
						a10 = []	
						for pessoa in (passageiroDao.getNome(nome.capitalize())):
							print(pessoa)
							a10.append(pessoa)
						if len(a10) == 0:
							print("Pessoa não encontrada!!")
					input("\nClique para voltar ao Menu!!")	
				elif escolha3 == '2':
					cpf = input("Digite o cpf")
					if len(cpf) == 0:
						p.semTexto()
						break

					else:
						a11 = []	
						for pessoa in (passageiroDao.getCpf(cpf)):
							a11.append(pessoa)
							print(pessoa)
						if len(a11) == 0:
							print("Pessoa não encontrada!!")
					input("\nClique para voltar ao Menu!!")	

				elif escolha3 == '3':
					while True:
						try:
							idade = int(input("Digite a idade:"))
							break
						except ValueError:
							print("Digite apenas números:")
					a12 = []		
					for pessoa in (passageiroDao.getIdade(idade)):
						print(pessoa)
						a12.append(pessoa)
					if len(a12) == 0:
						print("Pessoa não encontrada!!")
					input("\nClique para voltar ao Menu!!")	
		
			
		elif escolha == '7':
			sys.exit()		

			




						
							
							
				
								


									




				