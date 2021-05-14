from sound import *

def interpretador(input_text):
    l = input_text
    x=0 #ponteiro da lista
    nota = 'A' #nota inicial
    bpm = 100 #bpm inicial
    instrumento = 0 #instrumento inicial
    oitava = 1
    lista = []
    numeros = ['1','2','3','4','5','6','7','8','9','0']
    listaNotas = ['A','B','C','D','E','F','G']
    #tururu = Music(lista, volume, bpm, "Tururu")
    musica = Music()
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

        print("instrumento: " + str(instrumento)) #DEBUG
        lista.append((nota,oitava,instrumento))


    #AQUI TEM QUE FAZER A CONVERSÃO DO INSTRUMENTO INT PRA STR
    #terceiro elemento de cada elemento da lista é o instrumento
    #tem que passar pra string

    #x=0
    #while x<len(lista):
        #lista[x][x+3]=funcao que converte int pra string (nome do instrumento)

    print(lista) #DEBUG
    return lista


