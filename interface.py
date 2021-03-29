import PySimpleGUI as sg

class interface:

    play_button = sg.Button('Tocar música',font='halvetica',disabled=False)
    stop_button = sg.Button('Parar música',font='halvetica',disabled=True)
    text_box    = sg.Multiline(default_text='',size=(75, 25),font='halvetica')
    layout =[ [sg.Text (" ",size=(10, 1))],
            [sg.Text (" ",size=(14, 1)), sg.Text("TEXT-TO-BEEP",justification='center',size=(20, 1),font=['halvetica',30]), ],
            [text_box, ],
            [sg.Text (" ",size=(10, 1))],
            [sg.Text (" ",size=(20, 2)), play_button, sg.Text(" ",size=(10, 2)), stop_button, ],
            [sg.Text (" ",size=(10, 1))], ]
    window = sg.Window('Text-to-Beep', layout)
    event, values = window.read()

    def __init__(self):
        pass

    def play(self):
        interface.play_button.disabled = True
        interface.stop_button.disabled = False

    def stop(self):
        interface.play_button.disabled = False
        interface.stop_button.disabled = True

    def draw_and_update_window(self):
        #event, values = interface.window.read()
        pass