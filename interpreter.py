from sound import *
import os 



def interpreter(input_text):
    midi_info = MIDIInfo()
    instruments_list = list(midi_info.getMidiInstruments())
    x=0 #string pointer
    note = 'A' #standard note
    instrument = 0 #standard instrument 
    octave = 5  # standard octave
    song_list = []
    list_of_numbers = ['1','2','3','4','5','6','7','8','9','0']
    list_of_notes = ['A','B','C','D','E','F','G']
    
    
    while x < len(input_text):
    #===========================================instruments chars==============================
        if input_text[x] == "!":
            #instrument = "agogô"
            instrument = 113
            x = x+1
        elif input_text[x] == "\n":
            #instrument = "tubular bells"
            instrument = 14
            x = x+1
        elif input_text[x] == ";":
            #instrument = "pan flute"
            instrument = 75
            x = x+1
        elif input_text[x] == ",":
            #instrument = "church organ"
            instrument = 19
            x = x+1
        elif input_text[x] == "i" or input_text[x] == "I" or input_text[x] == "o" or input_text[x] == "O" or input_text[x] == "u" or input_text[x] == "U":
            #instrument = "harpsichord"
            instrument = 6
            x = x+1

    #===========================================notes changes==============================
        elif input_text[x] in list_of_notes:
            note = input_text[x]
            x=x+1
    #===========================================volume changes==============================
        elif input_text[x] == '-':
            note = '-'
            x = x + 1
        elif input_text[x] == " ":  #caso do espaço, dobra o volume
            note = " "
            x=x+1
    #===========================================octave changes==============================
        elif input_text[x] == "?":
            octave = octave+1
            x = x+1
    #===========================================instruments changes by numbers==============================
        elif input_text[x] in list_of_numbers:   #list_of_numbers é a lista de 0,1,2,3...
            instrument = instrument + int(input_text[x])
            x = x+1
    ##===========================================other chars==============================
        else:
            if input_text[x-1] in list_of_notes:
                note = input_text[x-1]
                x = x + 1
            else:
                note = "-"
                x = x+1

        #print("instrument: " + str(instrument)) #DEBUG
        song_list.append((note,octave,instruments_list[instrument]))

    return song_list

def create_music_object(input_text,name):
    song_list = interpreter(input_text)
    volume_standard = 100
    bpm_standard = 5
    obj_music_object = Music(song_list,volume_standard,bpm_standard,name)
    return obj_music_object




def play(input_text):
    music_object=create_music_object(input_text,"\\temp")
    rec = Recorder()
    path = os.getcwd()+"\\temp.mid"  #create a temp file in the same directory
    rec.recordMusic(music_object,path)
    return

def save(input_text,path):

    name= os.path.basename(path)

    print(name)
    music_object=create_music_object(input_text,name)
    rec = Recorder()
    rec.recordMusic(music_object,path)
    return




'''
Dá pra pegar o dicionário que contém todos os instruments e converter pra uma lista,
assim o código é o próprio índice dele. Exemplo:

midi_info = MIDIInfo()
instruments_list = list(midi_info.getMidiInstruments())
print(instruments_list[6]) #harpsichord
print(instruments_list[14]) #tubular bells
'''


#Exemplo de texto para usar em testes:
'''
ZZBZGZDZZZBZGZDZZZBZGZDCDZZZBZGZDZZZBZGZDZZZBZGZDCDZ

volume = 100
bpm = 100
name = "teste interpreter"
'''