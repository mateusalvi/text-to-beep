import interface as interface

def main():
    window = interface.interface
   
    while True:
        window.update_window(window)    #!!Checa e atualiza eventos e entradas na interface!!
        if (window.event == interface.sg.WIN_CLOSED): #!!Fecha o programa se o usuário fechar a janela!!
            break
    
if __name__ == "__main__":
    main()