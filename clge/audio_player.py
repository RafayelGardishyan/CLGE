from .setup import get_platform
from playsound import playsound

class AudioPlayer:
    def __init__(self, path_to_file, asyncr=True):
        self.path_to_file = path_to_file
        if get_platform() == "Windows":
            self.asyncr = not asyncr
        else:
            self.asyncr = True

    def play(self):
        playsound(self.path_to_file, self.asyncr)

    def __str__(self):
        return "Audio Player Object"
