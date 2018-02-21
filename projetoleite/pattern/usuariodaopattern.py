from abc import abstractmethod,ABC
class UsuarioDaoPattern(ABC):

	@abstractmethod
	def saveOrUpdate(self):
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
