import PySimpleGUI as sg

class interface:
    sg.theme('Light Blue 2')                                                                                                    #Definição do tema à ser usado
    #Definição dos botões
    play_button   = sg.Button('Tocar música', font='Helvetica', disabled=False, key='play_button')                                 #Estado inicial do botão play
    stop_button   = sg.Button('Parar música', font='Helvetica', disabled=True, key='stop_button')                                  #Estado inicial do botão Stop
    select_button = sg.FileBrowse('Carregar arquivo', font='Helvetica', key='select_button', file_types=(("Text Files", "*.txt"), ))
    export_button = sg.Button('Exportar MIDI', font='Helvetica', key='export_button')
    save_button = sg.FileSaveAs('Exportar MIDI', font='Helvetica', key='save_button',default_extension=".MIDI",file_types=(("MIDI Files", "*.midi"), ))


    text_box      = sg.Multiline(default_text='', size=(75, 25), font='Helvetica', key='text_box')                                 #Caixa de texto
    #Definição da interface
    layout =[[sg.Text (" ",size=(10, 1))],                                                                                     #Tabela com os elementos da interface (linhas e colunas)
             [sg.Text (" ",size=(14, 1)), sg.Text("TEXT-TO-BEEP",justification='center',size=(20, 1),font=['Helvetica',30]), ],
             [text_box,],
             [sg.Text (" ",size=(10, 1))],
             [sg.Text (" ",size=(20, 2)), play_button, sg.Text(" ",size=(10, 2)), stop_button],
             [sg.Text (" ",size=(20, 2)), sg.Input(key='file_saved', visible=False, enable_events=True,default_text = " "),save_button, sg.Input(key='file_selected', visible=False, enable_events=True), select_button],
             #[sg.Text (" ",size=(20, 2)),save_button,]
             #[sg.Text (" ",size=(20, 2)), sg.Input(key='file_saved', visible=False, enable_events=True,default_text = " "),save_button,],
             [sg.Text (" ",size=(10, 1))], ]
    window = sg.Window('Text-to-Beep', layout)                                                                                  #Cria a janela com os elementos acima
    event = 0                                                                                                                   #Inicializa variavel que recebe os eventos da janela
    values = 0                                                                                                                  #Outros valores usado para eventos

    def __init__(self):
        pass

    #play() altera o botão de play para DESABILITADO e os demais HABILITADO. Significando que o software esta reproduzindo a musica e nao deve receber nenhum outro input alem de STOP
    def play(self):
        self.window['play_button'].update(disabled=True)
        self.window['select_button'].update(disabled=True)
        self.window['export_button'].update(disabled=True)
        self.window['stop_button'].update(disabled=False)

    #Complementar à def play(self).
    def stop(self):
        self.window['play_button'].update(disabled=False)
        self.window['select_button'].update(disabled=False)
        self.window['export_button'].update(disabled=False)
        self.window['stop_button'].update(disabled=True)

    #Carrega um arquivo .txt e passa ele para a caixa de texto
    def openFile(self):
        file_path = self.values['file_selected']
        if (file_path != ''):
            file = open(file_path, "r")
            self.text_box.print(file.read())
            print('Debug: Arquivo Carregado')
        else:
            print('Debug: Problema ao carregar arquivo')



    #Metodo que retorna o texto que está na caixa de texto
    def returnText (self):
        return self.text_box.get()

    #update_window(self) checa para interações com a interface e armazena em EVENT e VALUES. Em seguida é feita a alteração visual necessária na interface.
    def update_window(self):
        self.event, self.values = self.window.read()

        if(self.event == "play_button"):
            interface.play(self)
        elif(self.event == "stop_button"):
            interface.stop(self)
        else:
            pass

    def save_File(self,input_text):
        self.event, self.values = self.window.read()

        #Ta com um bug que não salva o primeiro arquivo, só apartir do segundo funciona corretamente, não to conseguindo resolver por enquanto
        filename = self.values['file_saved']   #Pega o nome do arquivo, vai vir de values, que vem do botão de salvar como
        #print(filename) DEBUG
        arquivo = open(filename + ".midi",'w')  #Salva um arquivo .midi
        arquivo.write(input_text)               #Escreve nesse arquivo o texto que está na caixa
        sg.popup("Arquivo .midi salvo com sucesso!")






