from limite.tela_coordenador import TelaCoordenador
from entidades.coordenador import Coordenador
from entidades.organizador import Organizador
from persistencia.coordenadordao import CoordenadorDAO
from persistencia.organizadordao import OrganizadorDAO


class ControladorCoordenador:
    def __init__(self, controlador_sistema):
        self.__coordenadordao = CoordenadorDAO()
        self.__tela_coordenador = TelaCoordenador()
        self.__controlador_sistema = controlador_sistema
        self.__continua_nesse_menu = True

    def abre_tela(self):
        lista_opcoes = {'btn_voltar': self.voltar, 'btn_organizadores': self.organizadores,
                        'btn_locais': self.locais, 'btn_agendamentos': self.agendamentos,
                        'btn_cad_entidade': self.cadastra_entidade, 'btn_cad_organizador': self.cadastra_organizador,
                        'btn_cad_local': self.cadastra_local}
        self.__continua_nesse_menu = True
        while self.__continua_nesse_menu:
            lista_opcoes[self.__tela_coordenador.open()]()
            self.__tela_coordeador.close()

    def organizadores(self):
        if len(self.organizadores()) == 0:
            self.__tela_cadastro.show_message("Aviso!", "Não existem organizadores cadastrados.")
        else:
            lista_organizadores = list()
            for organizador in self.organizadores():
                lista_organizadores.append("\nNome do organizador: " + organizador.nome +
                                      "\nEmail do organizador: " + organizador.email)
            self.__tela_organizador.show_message("Listagem de Organizadores" + "\nTotal de organizadores "
                                             "cadastrados: " + str(len(self.organizadores())),
                                             "\n".join(lista_organizadores))

    @property
    def organizadores(self):
        return self.__organizadordao.get_all()
