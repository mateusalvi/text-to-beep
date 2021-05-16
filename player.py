import audioplayer as audioplayer
import os

_player = audioplayer.AudioPlayer(os.getcwd() + "\\temp.mid")

def playMusic():
    _player.play(_player)

def stopMusic():
    _player.stop()
