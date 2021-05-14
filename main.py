import interface as interface
import fileManager as fileManager
import interpreter as interpreter

def main():
    window = interface.interface
   
    while True:
        window.update_window(window)#!!Checa e atualiza eventos e entradas na interface!!

        #Se o botão Tocar música for pressionado:
        if (window.event == "play_button"):
            print('Debug: Tocando a musica')
            input_text = window.returnText(window)
            interpreter.interpretador(input_text)                   #Chama o interpretador passando o texto escrito na caixa
            #chamar o player( Return do interpretador() )
            window.stop(window)                                     #Ao terminar a reprodução, altera os botões ativos
            print('Debug: Fim da reprodução')

        #Se o botão Parar música for pressionado:
        elif (window.event == "stop_button"):
            #parar a reprodução
            print('Debug: Parou a música')

        #Se o botão Carregar Arquivo for pressionado:
        elif (window.event == "file_selected"):
            print('Debug: Carregar arquivo de texto')
            textFile = fileManager.operations.openFile(window.values['file_selected'])
            window.writeFileToTextBox(textFile, window)
            print('Debug: Arquivo texto carregado')

        #Se o botão Salvar MIDI for pressionado:
        elif (window.event == "file_saved"):
            print('Debug: Salvando arquivo MIDI')
            filePathAndName = window.values['file_saved']
            MIDIinput = window.returnText(window)#!!!!!!!!! aqui vai o interpretador, no momento só salva oque está escrito na text box
            fileManager.operations.saveMidi(MIDIinput, filePathAndName)
            print('Debug: Arquivo MIDI salvo')

        #!!Fecha o programa se o usuário fechar a janela, precisa estar no loop do main!!
        elif (window.event == interface.sg.WIN_CLOSED):
            print(window.event)
            print(window.values)
            break
        

if __name__ == "__main__":
    main()