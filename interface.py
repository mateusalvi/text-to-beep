import PySimpleGUI as sg

class interface:
    sg.theme('Light Blue 2')                                                                                                    #Definição do tema à ser usado
    #Definição dos botões
    __play_button   = sg.Button('Tocar música', font='Helvetica', disabled=False, key='play_button')                                 #Estado inicial do botão play
    __stop_button   = sg.Button('Parar música', font='Helvetica', disabled=True, key='stop_button')                                  #Estado inicial do botão Stop
    __select_button = sg.FileBrowse('Carregar arquivo', font='Helvetica', key='select_button', file_types=(("Text Files", "*.txt"), ))
    __save_button   = sg.FileSaveAs('Exportar MIDI', font='Helvetica', key='save_button',default_extension=".MIDI",file_types=(("MIDI Files", "*.midi"), ))
    __text_box        = sg.Multiline(default_text='', size=(75, 25), font='Helvetica', key='text_box')                                 #Caixa de texto
    #Definição da interface
    layout =[[sg.Text (" ",size=(10, 1))],                                                                                     #Tabela com os elementos da interface (linhas e colunas)
             [sg.Text (" ",size=(14, 1)), sg.Text("TEXT-TO-BEEP",justification='center',size=(20, 1),font=['Helvetica',30]), ],
             [__text_box,],
             [sg.Text (" ",size=(10, 1))],
             [sg.Text (" ",size=(20, 2)), __play_button, sg.Text(" ",size=(10, 2)), __stop_button],
             [sg.Text (" ",size=(20, 2)), sg.Input(key='file_saved', visible=False, enable_events=True,default_text = " "), __save_button, sg.Input(key='file_selected', visible=False, enable_events=True), __select_button],
             [sg.Text (" ",size=(10, 1))], ]
    window = sg.Window('Text-to-Beep', layout)                                                                                  #Cria a janela com os elementos acima
    event = 0                                                                                                                   #Inicializa variavel que recebe os eventos da janela
    values = 0                                                                                                                  #Outros valores usado para eventos

    def __init__(self):
        pass

    #play() altera o botão de play e demais para DESABILITADO e stop para HABILITADO. Significando que o software esta reproduzindo a musica e nao deve receber nenhum outro input alem de STOP
    def play(self):
        self.window['play_button'].update(disabled=True)
        self.window['select_button'].update(disabled=True)
        self.window['save_button'].update(disabled=True)
        self.window['stop_button'].update(disabled=False)

    #Complementar à def play(self).
    def stop(self):
        self.window['play_button'].update(disabled=False)
        self.window['select_button'].update(disabled=False)
        self.window['save_button'].update(disabled=False)
        self.window['stop_button'].update(disabled=True)
    
    def writeFileToTextBox (textFile, janela):
        if textFile != None:
            janela.__text_box.print(textFile.read())
        else:
            print("Debug: Carregamento de arquivo texto cancelado")

    #Metodo que retorna o texto que está na caixa de texto
    def returnText (self):
        return self.__text_box.get()

    #update_window(self) checa para interações com a interface e armazena em EVENT e VALUES. Em seguida é feita a alteração visual necessária na interface.
    def update_window(self):
        self.event, self.values = self.window.read()
        if(self.event == "play_button"):
            interface.play(self)
        elif(self.event == "stop_button"):
            interface.stop(self)
        else:
            pass






