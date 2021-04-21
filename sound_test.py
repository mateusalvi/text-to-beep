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

    def setUp(self):
        self.midi = MIDI(self.music_sample)
    
    def test_midiNoteCode_valid1(self):
        midi_note = self.midi.midiNoteCode('C', 0)
        self.assertEqual(0, midi_note)

    def test_midiNoteCode_valid2(self):
        midi_note = self.midi.midiNoteCode('G', 10)
        self.assertEqual(127, midi_note)

    '''
    def test_midiNoteCode_invalid(self):
        with self.assertRaises(ValueError):
            self.midi.midiNoteCode("G#", 10)
    '''

    def test_midiNoteCode_invalid_octave(self):
        midi_note = self.midi.midiNoteCode('G#', 10)
        self.assertEqual(None, midi_note)
    
    def test_midiNoteCode_invalid_note(self):
        midi_note = self.midi.midiNoteCode('K', 5)
        self.assertEqual(None, midi_note)
    
    def test_midiNoteCode_invalid_type1(self):
        midi_note = self.midi.midiNoteCode(5, 5)
        self.assertEqual(None, midi_note)
    
    def test_midiNoteCode_invalid_type2(self):
        midi_note = self.midi.midiNoteCode('C', 'G')
        self.assertEqual(None, midi_note)
    
    def test_midiInstrumentCode_valid1(self):
        midi_instrument = self.midi.midiInstrumentCode("acoustic grand piano")
        self.assertEqual(0, midi_instrument)
    
    def test_midiInstrumentCode_valid2(self):
        midi_instrument = self.midi.midiInstrumentCode("gunshot")
        self.assertEqual(127, midi_instrument)
    
    def test_midiInstrumentCode_invalid_instrument(self):
        midi_instrument = self.midi.midiInstrumentCode("violão")
        self.assertEqual(None, midi_instrument)
    
    def test_midiInstrumentCode_invalid_type(self):
        midi_instrument = self.midi.midiInstrumentCode(10)
        self.assertEqual(None, midi_instrument)

    def test_midiChannels_valid1(self):
        midi_channels = self.midi.midiChannels()
        self.assertEqual(1, midi_channels)
    
    def test_midiChannels_valid2(self):
        self.midi.setMusic(self.music_sample2)
        midi_channels = self.midi.midiChannels()
        self.assertEqual(4, midi_channels)

    #criar teste midichannels com musicas invalidas

    
if __name__ == "__main__":
     unittest.main()