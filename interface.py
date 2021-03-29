import PySimpleGUI as sg

class interface:
    sg.theme('Light Blue 2')                                                                                                    #Definição do tema à ser usado
    play_button = sg.Button('Tocar música',font='Helvetica',disabled=False,key='play_button')                                   #Estado inicial do botão play
    stop_button = sg.Button('Parar música',font='Helvetica',disabled=True,key='stop_button')                                    #Estado inicial do botão Stop
    text_box    = sg.Multiline(default_text='',size=(75, 25),font='Helvetica',key='text_box')                                   #Caixa de texto
    layout =[ [sg.Text (" ",size=(10, 1))],                                                                                     #Tabela com os elementos da interface (linhas e colunas)
            [sg.Text (" ",size=(14, 1)), sg.Text("TEXT-TO-BEEP",justification='center',size=(20, 1),font=['Helvetica',30]), ],
            [text_box, ],
            [sg.Text (" ",size=(10, 1))],
            [sg.Text (" ",size=(20, 2)), play_button, sg.Text(" ",size=(10, 2)), stop_button, ],
            [sg.Text (" ",size=(10, 1))], ]
    window = sg.Window('Text-to-Beep', layout)                                                                                  #Cria a janela com os elementos acima
    event = 0                                                                                                                   #Inicializa variavel que recebe os eventos da janela
    values = 0                                                                                                                  #Outros valores usado para eventos

    def __init__(self):
        pass

    #play() altera o botão de play para DESABILITADO e o de pausa para HABILITADO.
    def play(self):
        self.window['play_button'].update(disabled=True)
        self.window['stop_button'].update(disabled=False)
        self.event=0
    #Complementar à def play(self).
    def stop(self):
        self.window['play_button'].update(disabled=False)
        self.window['stop_button'].update(disabled=True)
        self.event=0

    #update_window(self) checa para interações com a interface e armazena em EVENT e VALUES. Em seguida é feita a alteração necessária na interface.
    def update_window(self):
        self.event, self.values = self.window.read()
        
        if(self.event == "play_button"):
            interface.play(self)
        elif(self.event == "stop_button"):
            interface.stop(self)
        else:
            pass
