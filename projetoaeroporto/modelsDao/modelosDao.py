from abc import abstractmethod,ABC

class Metodos(ABC):
    @abstractmethod
    def cadastrar(self):
        pass
    @abstractmethod
    def alterar(self):
        pass
    @abstractmethod
    def excluir(self):
        pass

    @abstractmethod
    def listar(self):
        pass
    
    
