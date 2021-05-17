import unittest
from sound import *

class RecorderTest(unittest.TestCase):
    song_of_healing =[  ('-',0,"ocarina"), # nota,oitava,instrumento
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
    music_sample = Music(song_of_healing, 100, 100, "Recorder_SoH")  #som,volume,bpm,
    #primeiro parametro é sounds que é a lista ali em cima

    def setUp(self):
        self.recorder = Recorder()
    
    def test_recordMusic(self):
        path = " "
        self.recorder.recordMusic(self.music_sample, path)

        midi = MIDIMusic()
        music_sample2 = Music(self.song_of_healing, self.music_sample.getVolume(), self.music_sample.getBPM(), "Recorder_Sample_File")
        midi.setMusic(music_sample2)
        midi.configMidiFile()
        midi.saveMidiFile(path)

        soh = open(path + self.music_sample.getName() + ".mid", "rb")
        soh2 = open(path + music_sample2.getName() + ".mid", "rb")

        self.assertEqual(type(soh), type(soh2))

        soh.close()
        soh2.close()


class MIDIInfoTest(unittest.TestCase):

    def setUp(self):
        self.midi_info = MIDIInfo()

    def test_noteCode_valid(self):
        note_code = self.midi_info.noteCode("C",5)
        self.assertEqual(note_code, 60)
    
    def test_noteCode_invalid(self):
        note_code = self.midi_info.noteCode("A",10)
        self.assertEqual(note_code, None)
    
    def test_instrumentCode_valid(self):
        instrument_code = self.midi_info.instrumentCode("Acoustic Grand Piano")
        self.assertEqual(instrument_code, 0)
    
    def test_instrumentCode_invalid(self):
        instrument_code = self.midi_info.instrumentCode("Violão")
        self.assertEqual(instrument_code, None)
    
    def test_isValidNote_valid(self):
        valid_note = self.midi_info.isValidNote("G")
        self.assertTrue(valid_note)
    
    def test_isValidNote_invalid(self):
        valid_note = self.midi_info.isValidNote("H")
        self.assertFalse(valid_note)
    
    def test_isValidOctave_valid(self):
        valid_octave = self.midi_info.isValidOctave("G", 5)
        self.assertTrue(valid_octave)
    
    def test_isValidOctave_invalid(self):
        valid_octave = self.midi_info.isValidOctave("G#", 10)
        self.assertFalse(valid_octave)
    
    def test_isValidInstrument_valid1(self):
        valid_instrument = self.midi_info.isValidInstrument("Gunshot")
        self.assertTrue(valid_instrument)
    
    def test_isValidInstrument_valid2(self):
        valid_instrument = self.midi_info.isValidInstrument(127)
        self.assertTrue(valid_instrument)
    
    def test_isValidInstrument_invalid1(self):
        valid_instrument = self.midi_info.isValidInstrument("Pandeiro")
        self.assertFalse(valid_instrument)
    
    def test_isValidInstrument_invalid2(self):
        valid_instrument = self.midi_info.isValidInstrument(128)
        self.assertFalse(valid_instrument)


class MIDIMusicTest(unittest.TestCase):
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
        self.midi_music = MIDIMusic(self.music_sample)

    def test_tracks_valid1(self):
        midi_tracks = self.midi_music._MIDIMusic__tracks()
        self.assertEqual(len(midi_tracks), 1)
    
    def test_tracks_valid2(self):
        self.midi_music.setMusic(self.music_sample2)
        midi_tracks = self.midi_music._MIDIMusic__tracks()
        self.assertEqual(len(midi_tracks), 4)
    
    def test_tracks_invalid1(self):
        self.midi_music.setMusic(self.music_sample_invalid1)
        midi_tracks = self.midi_music._MIDIMusic__tracks()
        self.assertEqual(midi_tracks, None)
    
    def test_tracks_invalid2(self):
        self.midi_music.setMusic(self.music_sample_invalid2)
        midi_tracks = self.midi_music._MIDIMusic__tracks()
        self.assertEqual(midi_tracks, None)
    
    def test_beat(self):
        beat = self.midi_music._MIDIMusic__beat()
        self.assertEqual(beat, 60 / self.music_sample.getBPM())
    
    def test_configMidiFile_valid(self):
        self.midi_music.configMidiFile()
        self.assertEqual(type(MIDIFile()), type(self.midi_music._MIDIMusic__midi_config))
    
    def test_configMidiFile_invalid1(self):
        self.midi_music.setMusic(self.music_sample_invalid1)
        self.midi_music.configMidiFile()
        self.assertEqual(None, self.midi_music._MIDIMusic__midi_config)
    
    def test_configMidiFile_invalid2(self):
        self.midi_music.setMusic(self.music_sample_invalid2)
        self.midi_music.configMidiFile()
        self.assertEqual(None, self.midi_music._MIDIMusic__midi_config)
    
    def test_saveMidiFile(self):
        path = " "
        self.midi_music.configMidiFile()
        self.midi_music.saveMidiFile(path)
        midi_file = open(path + self.music_sample.getName() + ".mid", "rb")

        sample_file = MIDIFile()
        with open(path + "MIDI_Sample_File.mid", "wb") as binfile:
            sample_file.writeFile(binfile)
        midi_file2 = open(path + "MIDI_Sample_File.mid", "rb")

        self.assertEqual(type(midi_file2), type(midi_file))

        midi_file.close()
        midi_file2.close()
    

if __name__ == "__main__":
     unittest.main()