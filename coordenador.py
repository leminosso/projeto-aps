class Coordenador:

    def __init__(self, nomeCoordenador: str, email: str, senha: str):
        self.__nomeCoordenador = nomeCoordenador
        self.__email = email
        self.__senha = senha

    @property
    def nomeCoordenador(self):
        return self.__nomeCoordenador

    @nomeCoordenador.setter
    def nomeCoordenador(self, nomeCoordenador: str):
        self.__nome = nomeCoordenador

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha