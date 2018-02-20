from .setup import get_platform
from playsound import playsound

class AudioPlayer:
    path_to_file = None
    async = False

    def __init__(self, path_to_file, async=True):
        self.path_to_file = path_to_file
        if get_platform() == "Windows":
            self.async = not async
        else:
            self.async = True

    def play(self):
        playsound(self.path_to_file, self.async)

    def __str__(self):
        return "Audio Player Object"
