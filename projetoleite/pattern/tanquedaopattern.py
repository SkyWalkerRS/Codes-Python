from abc import abstractmethod,ABC
class TanqueDaoPattern(ABC):
    @abstractmethod
    def saveOrUpdate(self):
        pass

    @abstractmethod
    def getTanque(self):
        pass

    @abstractmethod
    def getLista(self):
        pass


    @abstractmethod
    def getListaPesquisa(self):
        pass

    @abstractmethod
    def excluir(self):
        pass

    @abstractmethod
    def setCarga(self):
        pass

    
    @abstractmethod
    def getCarga(self):
        pass            
    
    
