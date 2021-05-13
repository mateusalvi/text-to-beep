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

        #To com um bug nessa função: o primeiro arquivo não é salvo, apenas do segundo em diante, ta passando um null que eu não to sabendo de onde vem e bugando o primeiro
        elif (window.event == "file_saved"):
            print('Debug: Salvando Arquivo')
            input_text = window.returnText(window)
            window.save_File(window,input_text)


        elif (window.event == interface.sg.WIN_CLOSED):#!!Fecha o programa se o usuário fechar a janela!!
            print(window.event)
            break
        

if __name__ == "__main__":
    main()