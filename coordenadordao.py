from persistencia.dao import DAO
from entidades.coordenador import Coordenador


class CoordenadorDAO(DAO):
    def __init__(self):
        super().__init__('coordenador.pkl')

    def add(self, key, coordenador: Coordenador):
        if (coordenador is not None) and (isinstance(key, int)):
            super().add(key, coordendor)

    def remove(self, coordenador: Coordenador):
        if (isinstance(coordenador, Coordenador)) and (Coordenador is not None):
            super().remove(coordenador.id)