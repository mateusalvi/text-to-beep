from sound import *
from Constants import *
import os

def interpreter(input_text):
    midi_info = MIDIInfo()
    instruments_list = list(Constants.INSTRUMENTS)
    x = 0 # string pointer
    note = Constants.DEFAULT_NOTE
    instrument = Constants.DEFAULT_INSTRUMENT
    octave = Constants.DEFAULT_OCTAVE
    song_list = []
    
    
    while x < len(input_text) - 1:
    #===========================================instruments chars==============================
        if input_text[x] in Constants.INSTRUMENT_MAPPINGS:
            instrument = Constants.INSTRUMENT_MAPPINGS[input_text[x]]
            x = x + 1

    #===========================================notes changes==============================
        elif input_text[x] in Constants.LIST_OF_NOTES:
            note = input_text[x]
            x = x + 1
    #===========================================volume changes==============================
        elif input_text[x] == '-':
            note = '-'
            x = x + 1
        elif input_text[x] == " ":  #caso do espaço, dobra o volume
            note = " "
            x = x + 1
    #===========================================octave changes==============================
        elif input_text[x] == "?":
            octave = octave + 1
            x = x + 1
    #================================instruments changes by numbers=========================
        elif input_text[x] in Constants.LIST_OF_NUMBERS:
            instrument = instrument + int(input_text[x])
            x = x + 1
    ##===========================================other chars================================
        else:
            if input_text[x-1] in Constants.LIST_OF_NOTES:
                note = input_text[x-1]
                x = x + 1
            else:
                note = "-"
                x = x + 1

        song_list.append((note, octave, instruments_list[instrument]))

    return song_list

def create_music_object(input_text,name):
    song_list = interpreter(input_text)
    obj_music_object = Music(song_list, Constants.DEFAULT_VOLUME, Constants.DEFAULT_BPM, name)
    return obj_music_object

def interpretToPlay(input_text):
    music_object = create_music_object(input_text, "\\temp.mid")
    rec = Recorder()
    path = os.getcwd() + "\\temp.mid"
    rec.recordMusic(music_object, path)
    return

def interpretToSave(input_text, path):
    name = os.path.basename(path)
    print(name)
    music_object = create_music_object(input_text, name)
    rec = Recorder()
    rec.recordMusic(music_object, path)
    return
