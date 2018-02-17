from settings import SOUND_FOLDER_PREFIX as sfp
from clge import AudioPlayer

def get_sounds():
    return {"sound1": AudioPlayer(sfp + "sound1.wav")}
