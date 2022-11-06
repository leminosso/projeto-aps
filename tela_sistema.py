from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaSistema(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def open(self): # -> 'mostra_menu'
        self.tela_opcoes() 
        botao, valores = self.__window.Read()
        if botao is None:
            botao = 0
        return botao, valores

    def tela_opcoes(self):
        sg.theme('Reddit')
        layout = [[sg.Text('Selecione seu papel'), sg.Combo(['Coordenador', 'Organizador', 'Aluno'], key='papel')],
                  [sg.Text('')],
                  [sg.Text('Email'), sg.Input(key='email')],
                  [sg.Text('Senha'), sg.Input(key='senha')],
                  [sg.Text('')],
                  [sg.Button('Confirmar', key='confirmar'), sg.Button('Cancelar', key='cancelar')]]
        self.__window = sg.Window("IsTeam's", element_justification='center', finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()
