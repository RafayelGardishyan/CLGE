import os
import json
from .exceptions import CLGEException
import zipfile
import os
import shutil

list = json.load(open(os.path.dirname(__file__) + "\plugs\plugs.json"))

def GetPlugins(list):
    plugins = ""
    for plugin in list:
        plugins += plugin + ". "
    return plugins


def UninstallPlugin(plugin_name):
    shutil.rmtree(os.path.dirname(__file__) + "\plugs\\" + plugin_name)
    list = json.load(open(os.path.dirname(__file__) + "\plugs\plugs.json"))
    list.pop(list.index(plugin_name))
    open(os.path.dirname(__file__) + "\plugs\plugs.json", "w+").write(json.dumps(list))


def PluginInstaller(plugin_full_path, plugin_name):
    with zipfile.ZipFile(plugin_full_path, "r") as z:
        os.makedirs(os.path.dirname(__file__) + "\plugs\\" + plugin_name)
        z.extractall(os.path.dirname(__file__) + "\plugs\\" + plugin_name)
        list = json.load(open(os.path.dirname(__file__) + "\plugs\plugs.json"))
        list.append(plugin_name)
        plugins = GetPlugins(list)
        print("Your installed plugins: {}".format(plugins))

        open(os.path.dirname(__file__) + "\plugs\plugs.json", "w+").write(json.dumps(list))


