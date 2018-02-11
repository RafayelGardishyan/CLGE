from settings import DATA_FILE
import json


def get_data():
    return json.load(open(DATA_FILE))
