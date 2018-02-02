from playsound import playsound

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
