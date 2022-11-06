from entidades.aluno import Aluno

class ControladorAluno:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__continua_nesse_menu = True