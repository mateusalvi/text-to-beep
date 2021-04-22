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
    song_of_healing =[ ('-',0,"ocarina"), 
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
    music_sample = Music(song_of_healing, 100, 100, "Song of Healing")
    music_sample2 = Music(test_sounds, 60, 60, "Music sample2")
    music_sample_invalid1 = Music([('A', 'ocarina')], 100, 100, "Music sample invalid 1")
    music_sample_invalid2 = Music([('A', 5, 8, 'ocarina')], 100, 100, "Music sample invalid 2")

    def setUp(self):
        self.midi = MIDI(self.music_sample)
    
    def test_noteCode_valid1(self):
        midi_note = self.midi._MIDI__noteCode('C', 0)
        self.assertEqual(0, midi_note)

    def test_noteCode_valid2(self):
        midi_note = self.midi._MIDI__noteCode('G', 10)
        self.assertEqual(127, midi_note)

    '''
    def test_noteCode_invalid(self):
        with self.assertRaises(ValueError):
            self.midi.__noteCode("G#", 10)
    '''

    def test_noteCode_invalid_octave(self):
        midi_note = self.midi._MIDI__noteCode('G#', 10)
        self.assertEqual(None, midi_note)
    
    def test_noteCode_invalid_note(self):
        midi_note = self.midi._MIDI__noteCode('K', 5)
        self.assertEqual(None, midi_note)
    
    def test_noteCode_invalid_type1(self):
        midi_note = self.midi._MIDI__noteCode(5, 5)
        self.assertEqual(None, midi_note)
    
    def test_noteCode_invalid_type2(self):
        midi_note = self.midi._MIDI__noteCode('C', 'G')
        self.assertEqual(None, midi_note)
    
    def test_instrumentCode_valid1(self):
        midi_instrument = self.midi._MIDI__instrumentCode("acoustic grand piano")
        self.assertEqual(0, midi_instrument)
    
    def test_instrumentCode_valid2(self):
        midi_instrument = self.midi._MIDI__instrumentCode("gunshot")
        self.assertEqual(127, midi_instrument)
    
    def test_instrumentCode_valid_uppercase(self):
        midi_instrument = self.midi._MIDI__instrumentCode("PICCOLO")
        self.assertEqual(72, midi_instrument)
    
    def test_instrumentCode_invalid_instrument(self):
        midi_instrument = self.midi._MIDI__instrumentCode("violão")
        self.assertEqual(None, midi_instrument)
    
    def test_instrumentCode_invalid_type(self):
        midi_instrument = self.midi._MIDI__instrumentCode(10)
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
        self.assertEqual(0.6, beat)
    
    def test_configMidiFile_valid(self):
        self.midi._MIDI__configMidiFile()
        self.assertEqual(type(MIDIFile()), type(self.midi._MIDI__midi_config))
    
    def test_configMidiFile_invalid1(self):
        self.midi.setMusic(self.music_sample_invalid1)
        self.midi._MIDI__configMidiFile()
        self.assertEqual(None, self.midi._MIDI__midi_config)
    
    def test_configMidiFile_invalid2(self):
        self.midi.setMusic(self.music_sample_invalid2)
        self.midi._MIDI__configMidiFile()
        self.assertEqual(None, self.midi._MIDI__midi_config)
    
    def test_saveMidiFile(self):
        self.midi._MIDI__configMidiFile()
        self.midi._MIDI__saveMidiFile()
        midi_file = open(self.music_sample.getName() + ".mid", "rb")
        sample_file = open("Sample File.mid", "rb")
        self.assertEqual(type(sample_file), type(midi_file))


   
if __name__ == "__main__":
     unittest.main()

