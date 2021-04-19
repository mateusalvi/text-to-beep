#from midiutil import MIDIFile

class Music:

    def __init__(self, notes=None, volume=None, bpm=None, name=None):
        self.__notes = notes
        self.__volume = volume
        self.__bpm = bpm
        self.__name = name
    

    def setVolume(self, volume):
        self.__volume = volume
    
    def getVolume(self):
        return self.__volume
    
    def setBPM(self, bpm):
        self.__bpm = bpm
    
    def getBPM(self):
        return self.__bpm
    
    def setName(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name
    
    def setNotes(self, notes):
        self.__notes = notes
    
    def getNotes(self):
        return self.__notes


class Recorder:

    def __init__(self, music=None): 
        self.midi = MIDI(music)
    
    def setMusic(self, music):
        self.midi.setMusic(music)
    
    def recordMusic(self):
        pass


class MIDI:

    def __init__(self, music=None):
        self.__music = music
    
    def setMusic(self, music):
        self.__music = music
    
    def getMusic(self):
        return self.__music
    
    def midiNote(self, note, octave):
    
        midicode = 0
        notes = {
            "C":0,
            "C#":1,
            "D":2,
            "D#":3,
            "E":4,
            "F":5,
            "F#":6,
            "G":7,
            "G#":8,
            "A":9,
            "A#":10,
            "B":11
        }

        midicode = notes[note] + (octave * 12)

        if(not(midicode >= 0 and midicode <= 127)):
            midicode = None
            raise KeyError("A nota não possui esta oitava!")
        
        return midicode