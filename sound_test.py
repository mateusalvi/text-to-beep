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
    
    def test_setNotes1(self):
        self.music.setNotes([('A',5,"acoustic grand piano")])
        self.assertListEqual([('A',5,"acoustic grand piano")], self.music.getNotes())
    
    def test_setNotes2(self):
        self.music.setNotes([('C',8,"harpsichord")])
        self.assertListEqual([('C',8,"harpsichord")], self.music.getNotes())


class MIDITest(unittest.TestCase):

    def setUp(self):
        self.midi = MIDI(Music([('C',8,"harpsichord")], 100, 60, "midi_music"))
    
    def test_midiNote1(self):
        midi_note = self.midi.midiNote("C", 5)
        self.assertEqual(60, midi_note)


if __name__ == "__main__":
     unittest.main()