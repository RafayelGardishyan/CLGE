import json
import os

"""
Get plugins list from plugs.json
"""
try:
    get_plugs = json.load(open(os.path.dirname(__file__) + "/plugs.json"))
except:
    get_plugs = json.load(open(os.path.dirname(__file__) + "plugs.json"))

"""
Export all plugins
"""
__all__ = get_plugs
