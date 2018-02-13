import json
import os

try:
    get_plugs = json.load(open(os.path.dirname(__file__) + "\plugs.json"))
except:
    get_plugs = json.load(open(os.path.dirname(__file__) + "plugs.json"))

__all__ = get_plugs
