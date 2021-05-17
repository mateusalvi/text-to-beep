from tkinter import font
from tkinter.constants import CENTER
import PySimpleGUI as sg

class interface:
    sg.theme('Light Blue 2')
    # Definição dos botões
    __play_button = sg.Button('Tocar música', font = 'Helvetica', disabled = False, key = 'play_button')
    __stop_button = sg.Button('Parar música', font = 'Helvetica', disabled = True, key = 'stop_button')
    __select_button = sg.FileBrowse('Abrir arquivo ', font = 'Helvetica', key = 'select_button', file_types = (("Text Files", "*.txt"), ))
    __save_button = sg.FileSaveAs('Exportar MIDI', font = 'Helvetica', key = 'save_button',default_extension = ".MIDI", file_types = (("MIDI Files", "*.midi"), ))
    __text_box = sg.Multiline(default_text = '', size = (75, 25), font = 'Helvetica', key = 'text_box')
    __octave_select = sg.Spin([i for i in range(1,10)], initial_value=5, font = 'Helvetica', key='octave_select', size=(2,1))
    __volume_slider = sg.Slider(range=(0,100), default_value=50, size=(15,15), orientation='horizontal', font=('Helvetica', 12), key='volume_slider')
    # Definição do layout da interface
    layout = [
        [sg.Text(" ", size = (10, 1))],
        [
            sg.Text(" ", size = (14, 1)),
            sg.Text("TEXT-TO-BEEP", justification = 'center', size = (20, 1), font = ['Helvetica', 30])
        ],
        [__text_box],
        [sg.Text(" ", size = (10, 1))],
        [
            sg.Text("Oitava inicial: ", size = (11, 1), font=('Helvetica', 12)),
            __octave_select,
            sg.Text(" ", size = (22, 1), pad='20'),
            __play_button, 
            sg.Text(" ", size = (10, 2)),
            __stop_button
        ],
        [
            sg.Text("Volume inicial:", size = (11, 1), font=('Helvetica', 12)),
            __volume_slider,
            sg.Text(" ", size = (5, 2)),
            sg.Input(key = 'file_saved', visible = False, enable_events = True, default_text = " "),
            __save_button,
            sg.Text(" ", size = (10, 2)),
            sg.Input(key = 'file_selected', visible = False, enable_events = True),
            __select_button
        ],
        [sg.Text(" ", size = (10, 1))]
    ]
    window = sg.Window('Text-to-Beep', layout)
    event = 0
    values = 0

    def __init__(self):
        pass

    # Altera os estados dos botões
    def play(self):
        self.window['play_button'].update(disabled = True)
        self.window['volume_slider'].update(disabled = True)
        self.window['octave_select'].update(disabled = True)
        self.window['select_button'].update(disabled = True)
        self.window['save_button'].update(disabled = True)
        self.window['stop_button'].update(disabled = False)

    # Altera os estados dos botões
    def stop(self):
        self.window['play_button'].update(disabled = False)
        self.window['volume_slider'].update(disabled = False)
        self.window['octave_select'].update(disabled = False)
        self.window['select_button'].update(disabled = False)
        self.window['save_button'].update(disabled = False)
        self.window['stop_button'].update(disabled = True)

    # Carrega um arquivo texto para a caixa de texto de entrada
    def writeFileToTextBox(self):
        textFile = None
        
        if self.values['file_selected'] != '':
            textFile = open(self.values['file_selected'], "r")
            if textFile != None:
                self.__text_box.print(textFile.read())
                textFile.close()        
        else: 
            pass

    # Metodo que retorna o texto que está na caixa de texto
    def returnText(self):
        return self.__text_box.get()

    def getDefaultVolumeSelect(self):
        return int(self.values['volume_slider'])
    
    def getDefaultOctaveSelect(self):
        return int(self.values['octave_select'])

    # update_window(self) checa para interações com a interface e armazena em EVENT e VALUES. Em seguida é feita a alteração visual necessária na interface.
    def update_window(self):
        self.event, self.values = self.window.read()
        if (self.event == "play_button"):
            interface.play(self)
        elif (self.event == "stop_button"):
            interface.stop(self)
        else:
            pass
