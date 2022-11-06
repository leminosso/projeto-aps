from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaCoordenador(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def open(self):
        self.tela_opcoes()
        button_key, values = self.__window.Read()
        if button_key is None:
            button_key = 0
        return (button_key)

    def tela_opcoes(self):
        sg.theme('Reddit')
        layout = [[sg.Text('')],
                  [sg.Button('Organizadores', key='btn_organizadores', font=('Helvetica', 12), border_width='0',
                    focus=(True, 'invisible')), sg.Button('Locais', key='btn_locais', font=('Helvetica', 12),
                    border_width='0', focus=(True, 'invisible')), sg.Button('Agendamentos da semana', key='btn_agendamentos',
                    font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))],
                  [sg.Text('')],
                  [sg.Button('Cadastrar Entidade', key='btn_cad_entidade', font=('Helvetica', 12), border_width='0',
                    focus=(True, 'invisible'))],
                  [sg.Button('Cadastrar Organizador', key='btn_cad_organizador', font=('Helvetica', 12), border_width='0',
                    focus=(True, 'invisible'))],
                  [sg.Button('Cadastrar Local', key='btn_cad_local', font=('Helvetica', 12), border_width='0',
                    focus=(True, 'invisible'))],
                  [sg.Text('')],
                  [sg.Button('Voltar', key='btn_voltar', font=('Helvetica', 12), border_width='0', focus=(True, 'invisible'))]]
        self.__window = sg.Window("Aba do Usuário", element_justification='center',
                                 finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()
