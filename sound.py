from midiutil import MIDIFile

class Music:

    def __init__(self, sounds=None, volume=None, bpm=None, name=None):
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


class Recorder:

    def __init__(self): 
        self.__midi = MIDI()
    
    def recordMusic(self, music):
        self.__midi.setMusic(music)
        self.__midi.configMidiFile()
        self.__midi.saveMidiFile()


class MIDI:

    def __init__(self, music=Music()):
        self.__music = music
        self.__midi_config = None
    
    def setMusic(self, music):
        self.__music = music
    
    def getMusic(self):
        return self.__music
    
    def getMidiNotes(self):
        midi_notes = {  
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
        
        return midi_notes
    
    def getMidiInstruments(self):
        midi_instruments = { 
            "acoustic grand piano":0, 
            "bright acoustic piano":1, 
            "electric grand piano":2, 
            "honky-tonk piano":3, 
            "electric piano 1":4, 
            "electric piano 2":5, 
            "harpsichord":6, 
            "clavi":7, 
            "celesta":8, 
            "glockenspiel":9, 
            "music box":10, 
            "vibraphone":11, 
            "marimba":12, 
            "xylophone":13, 
            "tubular bells":14, 
            "dulcimer":15, 
            "drawbar organ":16, 
            "percussive organ":17, 
            "rock organ":18, 
            "church organ":19, 
            "reed organ":20, 
            "accordion":21, 
            "harmonica":22, 
            "tango accordion":23, 
            "acoustic guitar (nylon)":24, 
            "acoustic guitar (steel)":25, 
            "electric guitar (jazz)":26, 
            "electric guitar (clean)":27, 
            "electric guitar (muted)":28, 
            "overdriven guitar":29, 
            "distortion guitar":30, 
            "guitar harmonics":31, 
            "acoustic bass":32, 
            "electric bass (finger)":33, 
            "electric bass (pick)":34, 
            "fretless bass":35, 
            "slap bass 1":36, 
            "slap bass 2":37, 
            "synth bass 1":38, 
            "synth bass 2":39, 
            "violin":40, 
            "viola":41, 
            "cello":42, 
            "contrabass":43, 
            "tremolo strings":44, 
            "pizzicato strings":45, 
            "orchestral harp":46, 
            "timpani":47, 
            "string ensemble 1":48, 
            "string ensemble 2":49, 
            "synth strings 1":50, 
            "synth strings 2":51, 
            "choir aahs":52, 
            "voice oohs":53, 
            "synth voice":54, 
            "orchestra hit":55, 
            "trumpet":56, 
            "trombone":57, 
            "tuba":58, 
            "muted trumpet":59, 
            "french horn":60, 
            "brass section":61, 
            "synth brass 1":62, 
            "synth brass 2":63, 
            "soprano sax":64, 
            "alto sax":65, 
            "tenor sax":66, 
            "baritone sax":67, 
            "oboe":68, 
            "english horn":69, 
            "bassoon":70, 
            "clarinet":71, 
            "piccolo":72, 
            "flute":73, 
            "recorder":74, 
            "pan flute":75, 
            "blown bottle":76, 
            "shakuhachi":77, 
            "whistle":78, 
            "ocarina":79, 
            "lead 1 (square)":80, 
            "lead 2 (sawtooth)":81, 
            "lead 3 (calliope)":82, 
            "lead 4 (chiff)":83, 
            "lead 5 (charang)":84, 
            "lead 6 (voice)":85, 
            "lead 7 (fifths)":86, 
            "lead 8 (bass + lead)":87, 
            "pad 1 (new age)":88, 
            "pad 2 (warm)":89, 
            "pad 3 (polysynth)":90, 
            "pad 4 (choir)":91, 
            "pad 5 (bowed)":92, 
            "pad 6 (metallic)":93, 
            "pad 7 (halo)":94, 
            "pad 8 (sweep)":95, 
            "fx 1 (rain)":96, 
            "fx 2 (soundtrack)":97, 
            "fx 3 (crystal)":98, 
            "fx 4 (atmosphere)":99, 
            "fx 5 (brightness)":100, 
            "fx 6 (goblins)":101, 
            "fx 7 (echoes)":102, 
            "fx 8 (sci-fi)":103, 
            "sitar":104, 
            "banjo":105, 
            "shamisen":106, 
            "koto":107, 
            "kalimba":108, 
            "bag pipe":109, 
            "fiddle":110, 
            "shanai":111, 
            "tinkle bell":112, 
            "agogô":113, 
            "steel drums":114, 
            "woodblock":115, 
            "taiko drum":116, 
            "melodic tom":117, 
            "synth drum":118, 
            "reverse cymbal":119, 
            "guitar fret noise":120, 
            "breath noise":121, 
            "seashore":122, 
            "bird tweet":123, 
            "telephone ring":124, 
            "helicopter":125, 
            "applause":126, 
            "gunshot":127 
        } 

        return midi_instruments
    
    def __noteCode(self, note, octave):
        midi_note_code = 0
        
        try:
            notes_dictionary = self.getMidiNotes()
            midi_note_code = notes_dictionary[note] + (octave * 12)

            if(not self.__isValidMIDINote(midi_note_code)):
                raise ValueError
        
        except KeyError:
            midi_note_code = None
            print(f"The note '{note}' is invalid!")
        
        except ValueError:
            midi_note_code = None
            print(f"'{note}' doesn't have a '{octave}' octave!")
        
        except:
            midi_note_code = None
            print("You put an invalid type argument!")

        finally:
            return midi_note_code
    
    def __isValidMIDINote(self, note):
        return (note >= 0 and note <= 127)

    def __instrumentCode(self, instrument): 
        
        try:
            midi_instruments_dictionary = self.getMidiInstruments()
            instrument = instrument.lower()

            midi_instrument = midi_instruments_dictionary[instrument]
        
        except:
            midi_instrument = None
            print(f"General MIDI doesn't have the '{instrument}' instrument!")
        
        finally:
            return midi_instrument

    def __tracks(self): 
        i_instrument = 2
        index = 0
        tracks = {}

        try:
            sound_list = self.__music.getSounds()

            for sound in sound_list:
                instrument = sound[i_instrument]

                if(self.__isValidMIDIInstrument(instrument)):
                    if(not instrument in tracks):
                        tracks[instrument] = index
                        index += 1
                else:
                    raise TypeError
        
        except:
            tracks = None
            print("You don't have a valid Music in your MIDI object!")
        
        finally:
            return tracks
    
    def __isValidMIDIInstrument(self, instrument):
        return instrument in self.getMidiInstruments()

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
            duration = self.__beat() #Change later to extend the notes sound
            volume = self.__music.getVolume()

            midi_config = MIDIFile(num_tracks)

            for sound in self.__music.getSounds():
                if(not self.__isSilence(sound[i_note])):
                    note = self.__noteCode(sound[i_note], sound[i_octave])
                    instrument = self.__instrumentCode(sound[i_instrument])
                    track = tracks[sound[i_instrument]]

                    midi_config.addNote(track, channel, note, time, duration, volume)
                    midi_config.addProgramChange(track, channel, time, instrument)

                time += duration
        
        except:
            midi_config = None
            print("You don't have a valid Music in your MIDI object!")

        finally:
            self.__midi_config = midi_config
    
    def __isSilence(self, note):
        return note == '-'

    def saveMidiFile(self):
        file_name = self.__music.getName() + ".mid" #Create a self.path in Records class to save the file wherever you want
        midi_config = self.__midi_config

        try:
            with open(file_name, "wb") as binfile:
                midi_config.writeFile(binfile)
        
        except:
            print("Invalid MIDI Config!")
        
        

