import interface as interface
import audioplayer as audioplayer
from interpreter import *
from PySimpleGUI.PySimpleGUI import R

def main():
    window = interface.interface
    
    while True:
        window.update_window(window)#Checa e atualiza eventos e entradas na interface

        #Se o botão Tocar música for pressionado:
        if (window.event == "play_button"):
            input_text = window.returnText(window)
            interpretToPlay(input_text)
            musicPlayer = audioplayer.AudioPlayer(os.getcwd()+"\\temp.mid") #inicializa o player
            musicPlayer.play()

        #Se o botão Parar música for pressionado:
        elif (window.event == "stop_button"):
            musicPlayer.stop()
            musicPlayer.close() #Finaliza o music player

        #Se o botão Carregar Arquivo for pressionado:
        elif (window.event == "file_selected"):
            window.writeFileToTextBox(window)

        #Se o botão Salvar MIDI for pressionado:
        elif (window.event == "file_saved"):
            filePathAndName = window.values['file_saved']
            input_text = window.returnText(window)
            interpretToSave(input_text,filePathAndName)

        #!!Fecha o programa se o usuário fechar a janela, precisa estar no loop do main!!
        elif (window.event == interface.sg.WIN_CLOSED):
            break        
        
if __name__ == "__main__":
    main()