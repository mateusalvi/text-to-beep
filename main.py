import interface as interface
import fileManager as fileManager
import audioplayer as audioplayer
import programa
import threading
import player
from interpreter import *

def main():
    #cria uma lista de threads
    threads = []

    #cria uma thread com o programa
    t = threading.Thread(target=programa.programa())
    #adiciona a thread à lista
    threads.append(t)
    #inicia a thread (e.g. executa Programa)
    t.start()

    #cria uma trhead para o Player de musica, que ficara rodando sem executar nada e faz as mesmas coisas de antes de adicionar a lista e iniciar
    t = threading.Thread(target=player())
    threads.append(t)
    t.start()

    #fecha as threads
    for process in threads:
    	process.join()
        
if __name__ == "__main__":
    main()