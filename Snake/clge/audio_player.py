from .exceptions import CLGEException
try:
    from playsound import playsound
except ImportError:
    raise CLGEException("No audio player. Please install it by \"pip install playsound\"")

class AudioPlayer:
    path_to_file = None
    async = False

    def __init__(self, path_to_file, async=True):
        self.path_to_file = path_to_file
        if async == True:
            self.async = False
        elif async == False:
            self.async = True

    def play(self):
        playsound(self.path_to_file, self.async)

    def __str__(self):
        return "Audio Player Object"
