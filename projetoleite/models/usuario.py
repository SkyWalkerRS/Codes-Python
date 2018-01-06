class Usuario(object):
    def __init__(self,cod,login,senha):	
        self.cod = cod
        self.login = login
        self.senha = senha

    def getCod(self):
        return self.cod

    def getLogin(self):
        return self.login

    def getSenha(self):
        return self.senha

    def __str__(self):
        return 'Cod:' + str(self.cod) + " | " + ' login:'+ self.login + ' | ' + " senha:" + self.senha
