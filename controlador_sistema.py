from limite.tela_sistema import TelaSistema
from controle.controlador_aluno import ControladorAluno
from controle.controlador_coordenador import ControladorCoordenador
from persistencia.coordenadordao import CoordenadorDAO


class ControladorSistema:
    __instance = None

    def __init__(self):
        self.__controlador_aluno = ControladorAluno(self)
        self.__controlador_coordenador = ControladorCoordenador(self)
        self.__tela_sistema = TelaSistema()

    def __new__(cls):
        if ControladorSistema.__instance is None:
            ControladorSistema.__instance = object.__new__(cls)
        return ControladorSistema.__instance

    def inicializa_sistema(self):
        self.tela_login()

    def tela_login(self):

        while True:
            botao, valores = self.__tela_sistema.open()
            if botao == sg.WIN_CLOSED or botao == 'Cancelar':
                break
            #verificar se o login é valido
            if botao == 'Confirmar':
                if valores["papel"] == 'Coordenador':
                    self.verificaLoginCoordenador(valores)
                elif valores["papel"] == 'Organizador':
                    self.verificaLoginOrganizador(valores)
                else:
                    self.verificaLoginAluno(valores)

    def verificaLoginCoordenador(self, valores):
        for coordenador in self.__coordenadordao.get_all():
            if coordenador.email == valores["email"]:
                if coordenador.senha == valores["senha"]:
                    self.coordenador()
                else:
                    raise SenhaInvalidaException
            else:
                raise EmailInvalidoException

    def coordenador(self):
        self.__controlador_coordenador.abre_tela()

    def organizador(self):
        self.__controlador_organizador.abre_tela()

    def aluno(self):
        self.__controlador_aluno.abre_tela()

    @property
    def controlador_coordenador(self):
        return self.__controlador_coordenador
