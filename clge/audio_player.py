from .exceptions import CLGEException
from .setup import get_platform
try:
    from playsound import playsound
except ImportError:
    raise CLGEException("No audio player. Please install it by \"pip install playsound\"")

class AudioPlayer:
    path_to_file = None
    async = False

    def __init__(self, path_to_file, async=True):
        self.path_to_file = path_to_file
        if get_platform() == "Windows":    
            if async == True:
                self.async = False
            elif async == False:
                self.async = True
        else:
            self.async = True

    def play(self):
        if get_platform() == "Windows":
            playsound(self.path_to_file, self.async)

    def __str__(self):
        return "Audio Player Object"
