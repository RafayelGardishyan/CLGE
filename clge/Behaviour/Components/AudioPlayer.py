from playsound import playsound
from .Component import Component
import asyncio

class AudioPlayer(Component):
    def __init__(self, path_to_file, loop=False, start_on_awake=False):
        self.loop = loop
        self.path_to_file = path_to_file

        self.my_type = "audioplayer"
        self.eventloop = asyncio.get_event_loop()

        if start_on_awake:
            self.play()

    def changeFile(self, path_to_file):
        self.path_to_file = path_to_file


    async def playTrack(self):
        playsound(self.path_to_file)
        if self.loop:
            asyncio.ensure_future(self.playTrack)

    def play(self):
        asyncio.ensure_future(self.playTrack)
        if self.loop:
            self.eventloop.run_forever()
        else:
            self.eventloop.run_until_complete(self.playTrack())

    def stop(self):
        self.eventloop.stop()
