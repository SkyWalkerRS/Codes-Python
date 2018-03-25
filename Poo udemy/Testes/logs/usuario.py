
import aula
import logging

class Usuario:

    def __init__(self, usuario, senha):
        
        self.usuario = usuario
        self.senha = senha
        self.dict_user = {'1':'Thomas', '2':'Marcos', '3':'José', '4':'QualquerNome'}

        format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        logging.basicConfig(filename="usuario.log", level=logging.DEBUG, filemode="w", format=format, datefmt="%d/%m/%Y %I:%M:%S %p")
        self.logger = logging.getLogger(__name__)

    def alterar_senha(self, nova_senha):
        
        self.senha = nova_senha
        self.logger.info("Alterada a senha!!")

    def autentica(self, usuario, senha):

        if self.usuario != usuario or self.senha != senha:
            self.logger.warning("Tentativa de acesso de inválida")
            return False
        return True

    def get_usuario_by_id(self, usuario_id):

        user = self.dict_user.get(usuario_id, None)
        if user is None:
            self.logger.error("Usuario id não existe: usuario_id={0}".format(usuario_id))
            return None
        return user

    def abrir_arquivo_usuario(self):

        try:
            open('/path/to/does/not/exist', 'rb')
        except (SystemExit, KeyboardInterrupt):
            raise
        except Exception as e:
            self.logger.exception("Error:")

    def algoritmo_complex(self, items):
        for i, item in enumerate(items):
            #faz algum complexo algoritmo_complex
            self.logger.debug('{0} iterator, item={1}'.format(i, item))

if __name__ == '__main__':
    user = Usuario("Thomas", "1234")
    user.alterar_senha("1255")
    user.autentica("Thomas", "324234")
    user.get_usuario_by_id("0")
    user.abrir_arquivo_usuario()
    user.algoritmo_complex([1,2,3,4])
    aula.execute()

