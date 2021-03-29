import interface as interface

def main():
    should_close = False
    window = interface.interface
   
    while (should_close != True):
        window.update_window(window)    #Checa e atualiza eventos e entradas na interface
        
    
if __name__ == "__main__":
    main()