from midiutil import MIDIFile
from Constants import *

class Music:
    def __init__(self, sounds = None, volume = None, bpm = None, name = None):
        self.__sounds = sounds
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

    def setSounds(self, sounds):
        self.__sounds = sounds

    def getSounds(self):
        return self.__sounds

    def toString(self): # for debug purposes
        print("=============================================================================")
        print("tupla de sons: " + str(self.__sounds))
        print("ultima elemento da tupla: " + str(self.__sounds[len(self.__sounds) - 1]))
        print("Volume: " + str(self.__volume))
        print("bpm: " + str(self.__bpm))
        print("nome: " + self.__name)
        print("=============================================================================")

class Recorder:
    def __init__(self): 
        self.__midi_music = MIDIMusic()
    
    def recordMusic(self, music, path):
        self.__midi_music.setMusic(music)
        self.__midi_music.configMidiFile()
        self.__midi_music.saveMidiFile(path)

class MIDIInfo:
    def __init__(self):
        pass

    def noteCode(self, note, octave):        
        try:
            if ((type(note) == str) and (type(octave) == int)):
                midi_note_code = Constants.MIDI_NOTES[note] + (octave * 12)

                if (not self.__isValidMIDINote(midi_note_code)):
                    raise ValueError
            else:
                raise TypeError
        
        except KeyError:
            midi_note_code = None
            print(f"The note '{note}' is invalid!")
        
        except ValueError:
            midi_note_code = None
            print(f"'{note}' doesn't have a '{octave}' octave!")
        
        except TypeError:
            midi_note_code = None
            print(f"'{note}' must be a string, and '{octave}' must be an int!")
        
        except:
            midi_note_code = None
            print("You put an invalid type argument!")

        finally:
            return midi_note_code
    
    def isValidOctave_LIMIT(self,octave,defaultOctaveSelect):
        if octave >= Constants.OCTAVE_LIMIT:
            octave = defaultOctaveSelect
            return octave
        else:
            return octave
    
    
    
    def __isValidMIDINote(self, note_code):
        if (type(note_code) == int):
            return (note_code >= 0 and note_code <= 127)
        else:
            return False

    def instrumentCode(self, instrument):   
        try:
            if (type(instrument) == str):
                instrument = instrument.lower()    
                midi_instrument_code = Constants.INSTRUMENTS[instrument]     
            else:
                raise TypeError
        
        except TypeError:
            midi_instrument_code = None
            print(f"'{instrument}' must be a string!")

        except:
            midi_instrument_code = None
            print(f"General MIDI doesn't have the '{instrument}' instrument!")
        
        finally:
            return midi_instrument_code

    def isValidNote(self, note):
        if (type(note) == str):
            return note in Constants.MIDI_NOTES
        else:
            return False

    def isValidOctave(self, note, octave):
        note_code = self.noteCode(note, octave)
        if (type(note_code) == int):
            return True
        else:
            return False
    
    def isValidInstrument(self, instrument):
        if (type(instrument) == str):
            return self.__isValidMIDIInstrument_str(instrument)   
        elif (type(instrument) == int):
            return self.__isValidMIDIInstrument_int(instrument)      
        else:
            return False
    
    def __isValidMIDIInstrument_str(self, instrument):
        if (type(instrument) == str):
            instrument = instrument.lower()
            return instrument in Constants.INSTRUMENTS
        else:
            return False
    
    def __isValidMIDIInstrument_int(self, instrument):
        if (type(instrument) == int):
            return (instrument >= 0 and instrument <= 127)
        else:
            return False

class MIDIMusic:
    def __init__(self, music = Music()):
        self.__music = music
        self.__midi_config = None
        self.__midi_info = MIDIInfo()
    
    def setMusic(self, music):
        self.__music = music
    
    def getMusic(self):
        return self.__music

    def __tracks(self): 
        i_instrument = 2
        index = 0
        tracks = {}

        try:
            sound_list = self.__music.getSounds()

            for sound in sound_list:
                instrument = sound[i_instrument]

                if (type(instrument) == str):
                    if (self.__midi_info.isValidInstrument(instrument)):
                        if (not instrument in tracks):
                            tracks[instrument] = index
                            index += 1
                    else:
                        raise KeyError
                else:
                    raise TypeError

        except TypeError:
            tracks = None
            print("The sound list of your Music don't have valid instruments, they must be strings!")
        
        except KeyError:
            tracks = None
            print(f"General MIDI doesn't have the '{instrument}' instrument!")
        
        except:
            tracks = None
            print("You don't have a valid Music in your MIDI object!")
        
        finally:
            return tracks

    def __beat(self):
        return 60 / self.__music.getBPM()
    
    def configMidiFile(self):
        i_note = 0
        i_octave = 1
        i_instrument = 2
        channel = 0
        time = 0

        try:
            tracks = self.__tracks()
            num_tracks = len(tracks)
            midi_config = MIDIFile(num_tracks)

            duration = self.__beat()
            volume = self.__music.getVolume()
            volume_def = volume

            for sound in self.__music.getSounds():
                if (not self.__isSilence(sound[i_note])):
                    if (not self.__isDoubleVolume(sound[i_note])):

                        note = self.__midi_info.noteCode(sound[i_note], sound[i_octave])
                        instrument = self.__midi_info.instrumentCode(sound[i_instrument])
                        track = tracks[sound[i_instrument]]

                        midi_config = self.__addSound(midi_config, track, channel, note, time, duration, volume, instrument)
                    
                    else:
                        volume = volume * 2
                        if (not self.__isValidVolume(volume)):
                            volume = volume_def
                        continue

                time += duration
        
        except:
            midi_config = None
            print("You don't have a valid Music in your MIDI object!")

        finally:
            self.__midi_config = midi_config
    
    def __isSilence(self, note):
        return note == '-'
    
    def __isDoubleVolume(self, note):
        return note == ' '
    
    def __isValidVolume(self, volume):
        return (volume >= 0 and volume <= 127)
    
    def __addSound(self, midi_file, track, channel, note, time, duration, volume, instrument):
        midi_file.addNote(track, channel, note, time, duration, volume)
        midi_file.addProgramChange(track, channel, time, instrument)
        return midi_file
    
    def saveMidiFile(self, path):
        file_name = self.__music.getName() + ".mid"
        midi_config = self.__midi_config

        try:
            with open(path, "wb") as binfile:
                midi_config.writeFile(binfile)
        
        except:
            print("Invalid MIDI Config!")
