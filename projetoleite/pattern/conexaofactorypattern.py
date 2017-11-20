from abc import abstractmethod,ABC
class ConexaoFactoryPattern(ABC):
	@abstractmethod
	def getConexao(self):
		pass

	@abstractmethod
	def criarTabelas(self):
		pass
		
	@abstractmethod
	def inicializarDados(self):
		pass
				