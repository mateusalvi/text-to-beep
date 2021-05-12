import interface as interface

def main():
    window = interface.interface
   
    while True:
        window.update_window(window)#!!Checa e atualiza eventos e entradas na interface!!
        

        if (window.event == "play_button"):
            print('Debug: Tocando a musica')
            input_text = window.returnText(window)
            #chamar o interpretador(passar texto)

        elif (window.event == "stop_button"):
            print('Debug: Parou a música')
            #parar a reprodução

        elif (window.event == "file_selected"): #Ao se escolher um arquivo, passa ele para a caixa de texto
            print('Debug: Carregar arquivo de texto')
            window.openFile(window)
        
        elif (window.event == "export_button"):
            print('Debug: Exportar para MIDI')
            input_text = window.returnText(window)
            #chamar a função exportar(texto)
    
        elif (window.event == interface.sg.WIN_CLOSED):#!!Fecha o programa se o usuário fechar a janela!!
            break
        

if __name__ == "__main__":
    main()