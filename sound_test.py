import unittest
from sound import *

class MusicTest(unittest.TestCase):
    
    def setUp(self):
        self.music = Music()

    def test_setVolume1(self):
        self.music.setVolume(10)
        self.assertEqual(10, self.music.getVolume())
    
    def test_setVolume2(self):
        self.music.setVolume(50)
        self.assertEqual(50, self.music.getVolume())
    
    def test_setBPM1(self):
        self.music.setBPM(60)
        self.assertEqual(60, self.music.getBPM())
    
    def test_setBPM2(self):
        self.music.setBPM(120)
        self.assertEqual(120, self.music.getBPM())
    
    def test_setName1(self):
        self.music.setName("abc")
        self.assertEqual("abc", self.music.getName())
    
    def test_setName2(self):
        self.music.setName("def")
        self.assertEqual("def", self.music.getName())
    
    def test_setSounds1(self):
        self.music.setSounds([('A',5,"acoustic grand piano")])
        self.assertListEqual([('A',5,"acoustic grand piano")], self.music.getSounds())
    
    def test_setSound2(self):
        self.music.setSounds([('C',8,"harpsichord")])
        self.assertListEqual([('C',8,"harpsichord")], self.music.getSounds())


class MIDITest(unittest.TestCase):
    song_of_healing =[  ('-',0,"ocarina"), 
                        ('-',0,"ocarina"), 
                        ('B',5,"ocarina"), 
                        ('-',0,"ocarina"), 
                        ('G',5,"ocarina"), 
                        ('-',0,"ocarina"),
                        ('D',5,"ocarina"),
                        ('-',0,"ocarina"),
                        ('-',0,"ocarina"), 
                        ('-',0,"ocarina"), 
                        ('B',5,"ocarina"), 
                        ('-',0,"ocarina"), 
                        ('G',5,"ocarina"), 
                        ('-',0,"ocarina"),
                        ('D',5,"ocarina"),
                        ('-',0,"ocarina"),
                        ('-',0,"ocarina"),
                        ('-',0,"ocarina"),
                        ('B',5,"ocarina"), 
                        ('-',0,"ocarina"), 
                        ('G',5,"ocarina"), 
                        ('-',0,"ocarina"),
                        ('D',5,"ocarina"),
                        ('C',5,"ocarina"),
                        ('D',5,"ocarina"),
                        ('-',0,"ocarina"), 
                        ('-',0,"ocarina"),
                        ('-',0,"ocarina"), 
                        ('B',5,"ocarina"), 
                        ('-',0,"ocarina"), 
                        ('G',5,"ocarina"), 
                        ('-',0,"ocarina"),
                        ('D',5,"ocarina"),
                        ('-',0,"ocarina"),
                        ('-',0,"ocarina"), 
                        ('-',0,"ocarina"), 
                        ('B',5,"ocarina"), 
                        ('-',0,"ocarina"), 
                        ('G',5,"ocarina"), 
                        ('-',0,"ocarina"),
                        ('D',5,"ocarina"),
                        ('-',0,"ocarina"),
                        ('-',0,"ocarina"),
                        ('-',0,"ocarina"),
                        ('B',5,"ocarina"), 
                        ('-',0,"ocarina"), 
                        ('G',5,"ocarina"), 
                        ('-',0,"ocarina"),
                        ('D',5,"ocarina"),
                        ('C',5,"ocarina"),
                        ('D',5,"ocarina")]
    test_sounds = [ ('-',0,"ocarina"),
                    ('C',1,"acoustic grand piano"),
                    ('E',2,"harpsichord"),
                    ('G',3,"violin")]
    
    music_sample = Music(song_of_healing, 100, 100, "MIDI_SoH")
    music_sample2 = Music(test_sounds, 60, 60, "Music sample2")
    
    music_sample_invalid1 = Music([('A', 'ocarina')], 100, 100, "Music sample invalid 1")
    music_sample_invalid2 = Music([('A', 5, 8, 'ocarina')], 100, 100, "Music sample invalid 2")

    def setUp(self):
        self.midi = MIDI(self.music_sample)
    
    def test_noteCode_valid1(self):
        midi_note = self.midi.noteCode('C', 0)
        self.assertEqual(0, midi_note)

    def test_noteCode_valid2(self):
        midi_note = self.midi.noteCode('G', 10)
        self.assertEqual(127, midi_note)

    def test_noteCode_invalid_octave(self):
        midi_note = self.midi.noteCode('G#', 10)
        self.assertEqual(None, midi_note)
    
    def test_noteCode_invalid_note(self):
        midi_note = self.midi.noteCode('K', 5)
        self.assertEqual(None, midi_note)
    
    def test_noteCode_invalid_type1(self):
        midi_note = self.midi.noteCode(5, 5)
        self.assertEqual(None, midi_note)
    
    def test_noteCode_invalid_type2(self):
        midi_note = self.midi.noteCode('C', 'G')
        self.assertEqual(None, midi_note)
    
    def test_instrumentCode_valid1(self):
        midi_instrument = self.midi.instrumentCode("acoustic grand piano")
        self.assertEqual(0, midi_instrument)
    
    def test_instrumentCode_valid2(self):
        midi_instrument = self.midi.instrumentCode("gunshot")
        self.assertEqual(127, midi_instrument)
    
    def test_instrumentCode_valid_uppercase(self):
        midi_instrument = self.midi.instrumentCode("PICCOLO")
        self.assertEqual(72, midi_instrument)
    
    def test_instrumentCode_invalid_instrument(self):
        midi_instrument = self.midi.instrumentCode("violão")
        self.assertEqual(None, midi_instrument)
    
    def test_instrumentCode_invalid_type(self):
        midi_instrument = self.midi.instrumentCode(10)
        self.assertEqual(None, midi_instrument)

    def test_tracks_valid1(self):
        midi_tracks = self.midi._MIDI__tracks()
        self.assertEqual(1, len(midi_tracks))
    
    def test_tracks_valid2(self):
        self.midi.setMusic(self.music_sample2)
        midi_tracks = self.midi._MIDI__tracks()
        self.assertEqual(4, len(midi_tracks))
    
    def test_tracks_invalid1(self):
        self.midi.setMusic(self.music_sample_invalid1)
        midi_tracks = self.midi._MIDI__tracks()
        self.assertEqual(None, midi_tracks)
    
    def test_tracks_invalid2(self):
        self.midi.setMusic(self.music_sample_invalid2)
        midi_tracks = self.midi._MIDI__tracks()
        self.assertEqual(None, midi_tracks)

    def test_beat(self):
        beat = self.midi._MIDI__beat()
        self.assertEqual(60 / self.music_sample.getBPM(), beat)
    
    def test_configMidiFile_valid(self):
        self.midi.configMidiFile()
        self.assertEqual(type(MIDIFile()), type(self.midi._MIDI__midi_config))
    
    def test_configMidiFile_invalid1(self):
        self.midi.setMusic(self.music_sample_invalid1)
        self.midi.configMidiFile()
        self.assertEqual(None, self.midi._MIDI__midi_config)
    
    def test_configMidiFile_invalid2(self):
        self.midi.setMusic(self.music_sample_invalid2)
        self.midi.configMidiFile()
        self.assertEqual(None, self.midi._MIDI__midi_config)
    
    def test_saveMidiFile(self):
        path = "/"
        self.midi.configMidiFile()
        self.midi.saveMidiFile(path)
        midi_file = open(self.music_sample.getName() + ".mid", "rb")

        sample_file = MIDIFile()
        with open("MIDI_Sample_File.mid", "wb") as binfile:
            sample_file.writeFile(binfile)
        midi_file2 = open("MIDI_Sample_File.mid", "rb")

        self.assertEqual(type(midi_file2), type(midi_file))

        midi_file.close()
        midi_file2.close()

    def test_isValidNote_valid(self):
        self.assertTrue(self.midi.isValidNote("A"))

    def test_isValidNote_invalid(self):
        self.assertFalse(self.midi.isValidNote("H"))

    def test_isValidOctave_valid(self):
        self.assertTrue(self.midi.isValidOctave("C", 5))
    
    def test_isValidOctave_invalid(self):
        self.assertFalse(self.midi.isValidOctave("A", 10))
    
    def test_isValidInstrument_valid1(self):
        self.assertTrue(self.midi.isValidInstrument("ocarina"))
    
    def test_isValidInstrument_valid2(self):
        self.assertTrue(self.midi.isValidInstrument(0))
    
    def test_isValidInstrument_invalid1(self):
        self.assertFalse(self.midi.isValidInstrument("violão"))
    
    def test_isValidInstrument_invalid2(self):
        self.assertFalse(self.midi.isValidInstrument(200))
    
    


   
class RecorderTest(unittest.TestCase):
    song_of_healing =[  ('-',0,"ocarina"), 
                        ('-',0,"ocarina"), 
                        ('B',5,"ocarina"), 
                        ('-',0,"ocarina"), 
                        ('G',5,"ocarina"), 
                        ('-',0,"ocarina"),
                        ('D',5,"ocarina"),
                        ('-',0,"ocarina"),
                        ('-',0,"ocarina"), 
                        ('-',0,"ocarina"), 
                        ('B',5,"ocarina"), 
                        ('-',0,"ocarina"), 
                        ('G',5,"ocarina"), 
                        ('-',0,"ocarina"),
                        ('D',5,"ocarina"),
                        ('-',0,"ocarina"),
                        ('-',0,"ocarina"),
                        ('-',0,"ocarina"),
                        ('B',5,"ocarina"), 
                        ('-',0,"ocarina"), 
                        ('G',5,"ocarina"), 
                        ('-',0,"ocarina"),
                        ('D',5,"ocarina"),
                        ('C',5,"ocarina"),
                        ('D',5,"ocarina"),
                        ('-',0,"ocarina"), 
                        ('-',0,"ocarina"),
                        ('-',0,"ocarina"), 
                        ('B',5,"ocarina"), 
                        ('-',0,"ocarina"), 
                        ('G',5,"ocarina"), 
                        ('-',0,"ocarina"),
                        ('D',5,"ocarina"),
                        ('-',0,"ocarina"),
                        ('-',0,"ocarina"), 
                        ('-',0,"ocarina"), 
                        ('B',5,"ocarina"), 
                        ('-',0,"ocarina"), 
                        ('G',5,"ocarina"), 
                        ('-',0,"ocarina"),
                        ('D',5,"ocarina"),
                        ('-',0,"ocarina"),
                        ('-',0,"ocarina"),
                        ('-',0,"ocarina"),
                        ('B',5,"ocarina"), 
                        ('-',0,"ocarina"), 
                        ('G',5,"ocarina"), 
                        ('-',0,"ocarina"),
                        ('D',5,"ocarina"),
                        ('C',5,"ocarina"),
                        ('D',5,"ocarina")]
    music_sample = Music(song_of_healing, 100, 100, "Recorder_SoH")

    def setUp(self):
        self.recorder = Recorder()
    
    def test_recordMusic(self):
        path = "/"
        self.recorder.recordMusic(self.music_sample, path)
        midi = MIDI()
        music_sample2 = Music(self.song_of_healing, self.music_sample.getVolume(), self.music_sample.getBPM(), "Recorder_Sample_File")
        midi.setMusic(music_sample2)
        midi.configMidiFile()
        midi.saveMidiFile(path)
        soh = open(self.music_sample.getName() + ".mid", "rb")
        soh2 = open(music_sample2.getName() + ".mid", "rb")

        self.assertEqual(type(soh), type(soh2))

        soh.close()
        soh2.close()

    



if __name__ == "__main__":
     unittest.main()



'''
song_of_healing =[  ('-',0,"ocarina"), 
                    ('-',0,"ocarina"), 
                    ('B',5,"ocarina"), 
                    ('-',0,"ocarina"), 
                    ('G',5,"ocarina"), 
                    ('-',0,"ocarina"),
                    ('D',5,"ocarina"),
                    ('-',0,"ocarina"),
                    ('-',0,"ocarina"), 
                    ('-',0,"ocarina"), 
                    ('B',5,"ocarina"), 
                    ('-',0,"ocarina"), 
                    ('G',5,"ocarina"), 
                    ('-',0,"ocarina"),
                    ('D',5,"ocarina"),
                    ('-',0,"ocarina"),
                    ('-',0,"ocarina"),
                    ('-',0,"ocarina"),
                    ('B',5,"ocarina"), 
                    ('-',0,"ocarina"), 
                    ('G',5,"ocarina"), 
                    ('-',0,"ocarina"),
                    ('D',5,"ocarina"),
                    ('C',5,"ocarina"),
                    ('D',5,"ocarina"),
                    ('-',0,"ocarina"), 
                    ('-',0,"ocarina"),
                    ('-',0,"ocarina"), 
                    ('B',5,"ocarina"), 
                    ('-',0,"ocarina"), 
                    ('G',5,"ocarina"), 
                    ('-',0,"ocarina"),
                    ('D',5,"ocarina"),
                    ('-',0,"ocarina"),
                    ('-',0,"ocarina"), 
                    ('-',0,"ocarina"), 
                    ('B',5,"ocarina"), 
                    ('-',0,"ocarina"), 
                    ('G',5,"ocarina"), 
                    ('-',0,"ocarina"),
                    ('D',5,"ocarina"),
                    ('-',0,"ocarina"),
                    ('-',0,"ocarina"),
                    ('-',0,"ocarina"),
                    ('B',5,"ocarina"), 
                    ('-',0,"ocarina"), 
                    ('G',5,"ocarina"), 
                    ('-',0,"ocarina"),
                    ('D',5,"ocarina"),
                    ('C',5,"ocarina"),
                    ('D',5,"ocarina")]
tururu = Music(song_of_healing, 100, 120, "Tururu")
path = "D:\\Arthur\\Área de Trabalho\\"

recorder = Recorder()
recorder.recordMusic(tururu, path)
'''


#Checar se os requisitos estão sendo atendidos. Mudança de volume, de instrumento e de oitava.
#Talvez seja necessário remover encapsulamento de alguns métodos

#-Espaço = Dobra o volume, se não volta pro padrão

#Melhorar checargem de tipos dos métodos, buscando remover as exceções.
#Checar repetição e usos de verificação de nota, oitava e instrumento