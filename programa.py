import interface as interface
from fileManager import *
import player
from interpreter import *

def programa():
    window = interface.interface
   
    while True:
        window.update_window(window) # Checa e atualiza eventos e entradas na interface!!

        # Se o botão Tocar música for pressionado:
        if (window.event == "play_button"):
            print('Debug: Tocando a musica')
            input_text = window.returnText(window)
            play(input_text)
            player.playMusic()
            print('Debug: Fim da reprodução')

        # Se o botão Parar música for pressionado:
        elif (window.event == "stop_button"):
            player.stopMusic()
            print('Debug: Parou a música')

        # Se o botão Carregar Arquivo for pressionado:
        elif (window.event == "file_selected"):
            print('Debug: Carregar arquivo de texto')
            textFile = Operations.openFile(window.values['file_selected'])
            window.writeFileToTextBox(textFile, window)
            print('Debug: Arquivo texto carregado')

        # Se o botão Salvar MIDI for pressionado:
        elif (window.event == "file_saved"):
            print('Debug: Salvando arquivo MIDI')
            filePathAndName = window.values['file_saved']
            input_text = window.returnText(window)
            save(input_text,filePathAndName)
            print('Debug: Arquivo MIDI salvo')

        # Fecha o programa se o usuário fechar a janela, precisa estar no loop do main!!
        elif (window.event == interface.sg.WIN_CLOSED):
            print(window.event)
            print(window.values)
            break
