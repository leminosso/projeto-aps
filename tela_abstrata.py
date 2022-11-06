from abc import ABC, abstractmethod
import PySimpleGUI as sg

class TelaAbstrata(ABC):

    @abstractmethod
    def tela_opcoes(self):  
        pass

    @abstractmethod
    def open(self):
        pass
        
    @abstractmethod
    def close(self):
        pass
   
    
    def show_message(self, titulo:str, mensagem: str):
        sg.Popup(titulo, mensagem)