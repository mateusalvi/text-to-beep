class operations:
    #Abre um arquivo com o nome e caminho recebidos
    def openFile(file_path):
        if (file_path != ""):
            file = open(file_path, "r")
            return file
        else:
            print('Debug: Nenhum arquivo texto selecionado')

    #Salva um arquivo com o nome, caminho e conteúdo recebidos
    def saveMidi(MIDIinput, filePathAndName):
        if filePathAndName != " ":
            arquivo = open(filePathAndName,'w')     #Salva um arquivo .midi, ja recebe a extensão .MIDI da janela de navegação chamada pela interface
            arquivo.write(MIDIinput)               #Escreve nesse arquivo o texto que está na caixa
            arquivo.close()
        else:
            print("Debug: Sem caminho especificado para salvar")


