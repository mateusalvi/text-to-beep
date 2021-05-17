Simple program that converts text to musical notes.

<b>Dictionary:</b><br/>
A, B, C, D, E, F, G - Root notes.<br/>
         ?          - Raise one octave. If over 9, octave is reset to chosen initial value.<br/>
   Numbers (1-9)    - Adds up the ID of the current instrument. (See instrument list at Constants.py)<br/>
   " " (Spacebar)   - Doubles the selected volume. If it goes over 100, volume is reset to chosen initial volume.<br/>
  "\n" (New line)   - Select instrument 15: Tubular bells.<br/>
        ;           - Select instrument 76: Pan flute.<br/>
        ,           - Select instrument 20: Church Organ.<br/>
        !           - Select instrument 114: Agogô.<br/>
 O, o, I, i, U, u   - Select instrument 7: Harpsichord<br/>
  All exceptions    - Repeat last note, if it's directly before, else it's silent.<br/>

<b>Necessary Libraries:</b><br/>
PySimpleGui - pip install pysimplegui<br/>
MIDIUtil - pip install MIDIUtil<br/>
Audio Player - pip install audioplayer<br/>

![Alt Text](https://cdn.discordapp.com/attachments/484444592502997012/777756020579631134/1604838266844.gif)
