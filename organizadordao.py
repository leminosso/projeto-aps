from persistencia.dao import DAO
from entidades.organizador import Organizador


class OrganizadorDAO(DAO):
    def __init__(self):
        super().__init__('organizador.pkl')

    def add(self, key, organizador: Organizador):
        if (organizador is not None) and (isinstance(key, int)):
            super().add(key, organizador)

    def remove(self, organizador: Organizador):
        if (isinstance(organizador, Organizador)) and (Organizador is not None):
            super().remove(organizador.id)