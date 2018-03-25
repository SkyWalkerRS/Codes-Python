

import logging

def execute():
	format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s' #filemod sobrescreve o log
	logging.basicConfig(filename="hello.log", level=logging.DEBUG, filemode="w", format=format, datefmt="%d/%m/%Y %I:%M:%S %p")
	logger = logging.getLogger(__name__)

	logger.info("Mensagem informativa")
	logger.debug("Mensagem de debug")
	logger.error("Um erro aconteceu.")

if __name__ == '__main__':
	execute()


