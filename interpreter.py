from sound import *
import os #pra salvar o arquivo temporario na mesma pasta

def interpretador(input_text):
    midi_info = MIDIInfo()
    lista_instrumentos = list(midi_info.getMidiInstruments())
    l = input_text
    x=0 #ponteiro da lista
    nota = 'A' #nota inicial
    bpm = 100 #bpm inicial
    volume = 100
    instrumento = 0 #instrumento inicial
    oitava = 1
    lista = []
    numeros = ['1','2','3','4','5','6','7','8','9','0']
    listaNotas = ['A','B','C','D','E','F','G']
    #tururu = Music(lista, volume, bpm, "Tururu")
    #musica = Music(lista,volume,100,"TESTE OI")



    l="ZZBZGZDZZZBZGZDZZZBZGZDCDZZZBZGZDZZZBZGZDZZZBZGZDCDZ"

    volume = 100
    bpm = 100
    nome = "teste interpretador"

    musica = Music(l,volume,bpm,nome)


    while x < len(l):

    #===========================================INSTRUMENTOS==============================
        if l[x] == "!":
            #instrumento = "agogô"
            instrumento = 113
            x = x+1
        elif l[x] == "\n":
            #instrumento = "tubular bells"
            instrumento = 14
            x = x+1
        elif l[x] == ";":
            #instrumento = "pan flute"
            instrumento = 75
            x = x+1
        elif l[x] == ",":
            #instrumento = "church organ"
            instrumento = 19
            x = x+1
        elif l[x] == "i" or l[x] == "I" or l[x] == "o" or l[x] == "O" or l[x] == "u" or l[x] == "U":
            #instrumento = "harpsichord"
            instrumento = 6
            x = x+1

    #===========================================NOTAS==============================
        elif l[x] in listaNotas:
            nota = l[x]
            x=x+1
    #===========================================VOLUME==============================
        elif l[x] == '-':
            nota = '-'
            x = x + 1
        elif l[x] == " ":  #caso do espaço, dobra o volume
            nota = " "
            x=x+1
    #===========================================OITAVAS==============================
        elif l[x] == "?":
            oitava = oitava+1
            x = x+1
    #===========================================TROCA DE INSTRUMENTO POR NÚMERO==============================
        elif l[x] in numeros:   #numeros é a lista de 0,1,2,3...
            instrumento = instrumento + int(l[x])
            x = x+1
    ##===========================================CONSOANTE / OUTROS CARACTÉRES==============================
        else:
            if l[x-1] in listaNotas:
                nota = l[x-1]
                x = x + 1
            else:
                nota = "-"
                x = x+1

        #print("instrumento: " + str(instrumento)) #DEBUG
        lista.append((nota,oitava,lista_instrumentos[instrumento]))
    #print(lista)
    musica.setSounds(lista)
    return musica

def play(input_text):
    musica=interpretador(input_text)
    rec = Recorder()
    path = os.getcwd() #vai salvar na mesma pasta o qual foi executado
    rec.recordMusic(musica,path)
    return






'''
Dá pra pegar o dicionário que contém todos os instrumentos e converter pra uma lista,
assim o código é o próprio índice dele. Exemplo:

midi_info = MIDIInfo()
lista_instrumentos = list(midi_info.getMidiInstruments())
print(lista_instrumentos[6]) #harpsichord
print(lista_instrumentos[14]) #tubular bells
'''


#Exemplo de texto para usar em testes:
'''
ZZBZGZDZZZBZGZDZZZBZGZDCDZZZBZGZDZZZBZGZDZZZBZGZDCDZ

volume = 100
bpm = 100
nome = "teste interpretador"
'''