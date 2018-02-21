import shlex
from datetime import datetime as datahora
from LDE import Dnodo, LDE
# Desafio 2 - TaskList
# Feitos - add - list - annotate - info###

def validaData(data_str):
    try:
      data = datahora.strptime(data_str, '%d/%m/%Y')
      return data
    except Exception as e:
        raise TypeError('Problema na formatacao da data')

class Task:    
    def __init__(self,
                 id,
                 titulo,
                 descricao = None,
                 completada = False,
                 prazo = None,
                 tags = [],
                 data_modificacao = datahora.now().strftime('%d/%m/%Y %H:%M:%S')):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.completada = completada
        self.prazo = prazo
        self.tags = tags
        self.data_modificacao = data_modificacao

    def __str__(self):
        # quando dermos print no objeto Task, mostrará:
        #id, titulo, prazo,completada
        retorno = ""
        retorno = retorno + 'Tarefa id: ' + str(self.id) + '\nTitulo: ' + self.titulo   
        if(self.prazo != None):
            retorno = retorno + '\nPrazo: ' + self.prazo
        else:
            retorno = retorno + '\nPrazo: Sem Prazo'

        if(self.completada):
            retorno = retorno + '\nCompletada: Sim'
        else:
            retorno = retorno + '\nCompletada: Não'


        return retorno

    def __lt__(self, other):
        return self.id < other.id
    
    def __le__(self, other):
        return self.id <= other.id
        
    def __eq__(self, other):
        return self.id == other.id
        
    def __ne__(self, other):        
        return self.id != other.id
        
    def __gt__(self, other):
        return self.id > other.id
        
    def __ge__(self, other):
        return self.id >= other.id    
    
class Console:
    def __init__(self, tasklist):
        self.tasklist = tasklist
    
    def prefix(self):
        return '\ntask> '

    def waitCommand(self):        
        comm = input(self.prefix())
        comm = comm.strip()
        return comm
        
    def start(self):
        print('== App de Tarefas :) ==')
        print('.. Console de comando inicializado ..')
           
    def parseCommand(self, comm):
        if comm.startswith(('help','?', '--help')):
            print('\n::.. Lista de comandos / Usando o app ..::')
            comandos = [
                '\thelp ou --help ou ?             - Esta tela de ajuda!',
                '\texit ou quit ou sair            - Finaliza o aplicativo',
                '\tadd <titulo>                    - Adiciona nova tarefa',
                '\tannotate <id> <nova_descricao>  - ...',
                '\tedit <id>                       - ...',
                '\tdelete <id>                     - ...',
                '\tlist                            - Lista todas as tarefas',                
                '\tinfo <id>                       - ...',
                '\tdone <id>                       - Marca tarefa como completada',
                '\tsort <ordem>                    - Ordenação: asc ou desc'
            ]
            
            for item in comandos:
                print(item)
            
        elif comm.startswith('add'):            
            # verifica os demais argumentos, separados por espaço
            try:
                args = shlex.split(comm)
                if len(args) < 2:
                    print('[Aviso] Verifique a sintaxe com comando: help')
                else:
                    id = self.tasklist.nextId()
                    self.tasklist.inserir(Task(id,args[1]))
                    # criar nova tarefa e inserí-la na lista (self.tasklist)
                    
            except ValueError as v:
                if str(v) == 'No closing quotation':
                    print('[Aviso] Verifique as aspas duplas')

        elif comm.startswith('annotate'):
            try:
                args = shlex.split(comm)
                if len(args) < 3:
                    print('[Aviso] Verifique a sintaxe com comando: help')
                else:          
                    try:          
                        tarefa = self.tasklist.findById(args[1])
                        tarefa.data_modificacao = datahora.now().strftime('%d/%m/%Y %H:%M:%S')                    
                        tarefa.descricao = args[2]
                    except:
                        print("ID não existe")
                    return 0    
                    # apos buscar a tarefa
                    # alterar a descricao da tarefa para o novo valor
                    # passado pelo usuario pela linha de comando
                    
            except ValueError as v:
                if str(v) == 'No closing quotation':
                    print('[Aviso] Verifique as aspas duplas')

        elif comm.startswith('list'):
            self.tasklist.listar()

        elif comm.startswith('edit'):
           
                args = shlex.split(comm)
                if len(args) < 2:
                    print('[Aviso] Verifique a sintaxe com comando: help')
                else:
                        id = args[1]
                        tarefa = self.tasklist.findById(id)
                        if tarefa == None:
                            print("Não existe esse Id..")
                        else:     
                            while True:
                                escolha = input('''Digite:
                                \n1 para editar o título
                                \n2 para editar a descrição
                                \n3 para definir completado ou não
                                \n4 para definir o prazo
                                \n5 para definir as tags
                                \n6 para sair''')
                                if(escolha == '6'):
                                    break;
                                elif (escolha == '1'):
                                    novtitulo = input("Título atual: "+tarefa.titulo+" \nDigite o novo título:")
                                    tarefa.titulo = novtitulo
                                    tarefa.data_modificacao = datahora.now().strftime('%d/%m/%Y %H:%M:%S')   
                                    break;
                                elif (escolha == '2'):
                                    novdescricao = input("descrição atual: "+str(tarefa.descricao)+" \nDigite a nova descrição:")
                                    tarefa.descricao = novdescricao
                                    tarefa.data_modificacao = datahora.now().strftime('%d/%m/%Y %H:%M:%S')   
                                    break;
                                elif (escolha == '3'):
                                    while True:
                                        nov = input("Completado :"+str(tarefa.completada)+"\nDigite S para Completo ou N para não completo:")
                                        if(nov=="S" or nov=="s"):
                                            tarefa.completada = True
                                            tarefa.data_modificacao = datahora.now().strftime('%d/%m/%Y %H:%M:%S')
                                            break;
                                        elif(nov=="N" or nov=="n"):
                                            tarefa.completada = False
                                            tarefa.data_modificacao = datahora.now().strftime('%d/%m/%Y %H:%M:%S')
                                            break;
                                        else:
                                            print("valor incorreto")
                                elif (escolha == '4'):
                                    nov = input("Prazo atual:"+str(tarefa.prazo)+"\nDigite o novo Prazo:")
                                    tarefa.prazo = nov
                                    tarefa.data_modificacao = datahora.now().strftime('%d/%m/%Y %H:%M:%S')   
                                    break;
                                elif (escolha == '5'):
                                    nov = input("tag atual:"+str(tarefa.tags)+"Digite o novo tag:")
                                    tags = shlex.split(nov)
                                    tarefa.tags = []
                                    for tag in tags:                                
                                        tarefa.tags.append(tag)                                
                                    tarefa.data_modificacao = datahora.now().strftime('%d/%m/%Y %H:%M:%S')   
                                    break;        
             

        elif comm.startswith('info'):
            try:
                args = shlex.split(comm)
                if len(args) < 2:
                    print('[Aviso] Verifique a sintaxe com comando: help')
                else:                    
                    resultado = self.tasklist.findById(args[1])    
                    if (resultado ==None):
                        print("Não existe este id..")
                    else:
                                            
                        retorno =''
                        try:
                            retorno = retorno + 'Tarefa id: ' + str(resultado.id) + '\nTitulo: ' + resultado.titulo   
                            if(resultado.prazo != None):
                                retorno = retorno + '\nPrazo: ' + resultado.prazo
                            else:
                                retorno = retorno + '\nPrazo: Sem Prazo'
                            if(resultado.completada):
                                retorno = retorno + '\nCompletada: Sim'
                            else:
                                retorno = retorno + '\nCompletada: Não'
                            retorno = retorno + '\nTags: '+ str(resultado.tags)
                            retorno = retorno + '\nDescrição: '+ str(resultado.descricao)
                            retorno = retorno + '\nData De modificação: ' + resultado.data_modificacao
                                
                                
                                    
                                
                        finally:
                            print(retorno)

                    
                   
                    
                    
                    
            except ValueError as v:
                if str(v) == 'No closing quotation':
                    print('[Aviso] Verifique as aspas duplas')
            
        elif comm.startswith('done'):
            try:
                args = shlex.split(comm)
                if len(args) < 2:
                    print('[Aviso] Verifique a sintaxe com comando: help')
                else:
                    ## busca por id
                    id = args[1]
                    tarefa = self.tasklist.findById(id)                    
                    if tarefa.completada == False:
                        tarefa.completada = True
                        tarefa.data_modificacao = datahora.now().strftime('%d/%m/%Y %H:%M:%S')         
                    else:
                        print("tarefa ja foi completada")
                       
                    # setar tarefa como concluida
                
            except ValueError as v:
                if str(v) == 'No closing quotation':
                    print('[Aviso] Verifique as aspas duplas')

        elif comm.startswith('delete'):
            try:
                args = shlex.split(comm)
                if len(args) < 2:
                    print('[Aviso] Verifique a sintaxe com comando: help')
                else:
                    id = args[1]
                    self.tasklist.delete(id)
                    #pass
                
            except ValueError as v:
                if str(v) == 'No closing quotation':
                    print('[Aviso] Verifique as aspas duplas')

        elif comm.startswith('sort'):
            try:
                args = shlex.split(comm)
                if len(args) < 2:
                    print('[Aviso] Verifique a sintaxe com comando: help')
                else:                    
                    ordem = args[1]
                    if ordem in ['asc', 'desc']:                        
                        # chama metodo de ordenacao, usando como criterio
                        # a forma de ordenacao passada na linha de comando

                        self.tasklist.sort(ordem)
                    else:
                        print('[Aviso] valores para ordem deverao ser: asc ou desc')
                    
            except ValueError as v:
                if str(v) == 'No closing quotation':
                    print('[Aviso] Verifique as aspas duplas')

        elif comm.startswith(('exit','sair')):
            exit(0)
            
        else:
            print('Não entendi... Melhor digitar: help')

class TaskList(LDE): # esta classe herda todos os metodos de LDE
    _id = 0   
    
    def nextId(self):
        self._id += 1 # incrementa campo _id
        return self._id

    def listar(self):
        # chama o método imprimir presente na classe LDE (arquivo separado)
        super().imprimir()

    def inserir(self, tarefa):
        # verifica se o parametro é um objeto do tipo Task
        if isinstance(tarefa, Task):
            
            # chama inserir da classe LDE (arquivo separado)           
            super().inserirFim(Dnodo(tarefa))
        else:
            raise TypeError('objeto nao e\' do tipo Task')

    def findById(self, id):                
        item = self.header.next        

        # realiza a busca sequencial por um item que possui o id mencionado
        while (item is not self.trailer):            
            if isinstance(item.dado, Task):                
                if str(item.dado.id) == str(id):
                    return item.dado
            else:
                raise TypeError('objeto nao e\' do tipo Task')
            
            item = item.next
            
    def delete(self, id):        
       x = self.findById(id)
       self.remover(x)        
        # obtem a referencia para o objeto a partir do id (usar o metodo findById)
        # apos chama o metodo remover presente na classe LDE
        #pass

    def sort(self, ordem): #bubble sort
        self.sorts(ordem)
                
# ----------------------------------------------------------------
# Método main, a execucao inicia por aqui !! #
def main():    
    console = Console( TaskList() )
    console.start()
    while True:
        comm = console.waitCommand()
        console.parseCommand(comm)
    
if __name__ == '__main__':
    main()
