import os
import json
from .exceptions import CLGEException
import zipfile
import os
import shutil

path = os.path.dirname(__file__)

try:
    list = json.load(open(path + "/plugs/plugs.json"))
except:
    list = json.load(open(path + "plugs/plugs.json"))


def GetPlugins(list):
    plugins = ""
    for plugin in list:
        plugins += plugin + " "
    return plugins


def UninstallPlugin(plugin_name):
    try:
        shutil.rmtree(path + r"/plugs/" + plugin_name)
        list = json.load(open(path + "/plugs/plugs.json"))
        list.pop(list.index(plugin_name))
        open(path + "/plugs/plugs.json", "w+").write(json.dumps(list))
    except:
        shutil.rmtree(path + r"plugs/" + plugin_name)
        list = json.load(open(path + "plugs/plugs.json"))
        list.pop(list.index(plugin_name))
        open(path + "plugs/plugs.json", "w+").write(json.dumps(list))


def PluginInstaller(plugin_full_path, plugin_name):
    with zipfile.ZipFile(plugin_full_path, "r") as z:
        try:
            os.makedirs(path + r"/plugs/" + plugin_name)
            z.extractall(path + r"/plugs/" + plugin_name)
            list = json.load(open(path + "/plugs/plugs.json"))
            list.append(plugin_name)
            plugins = GetPlugins(list)
            print("Your installed plugins: {}".format(plugins))
            open(path + "/plugs/plugs.json", "w+").write(json.dumps(list))
        except:
            os.makedirs(path + r"plugs/" + plugin_name)
            z.extractall(path + r"plugs/" + plugin_name)
            list = json.load(open(path + "plugs/plugs.json"))
            list.append(plugin_name)
            plugins = GetPlugins(list)
            print("Your installed plugins: {}".format(plugins))
            open(path + "/plugs/plugs.json", "w+").write(json.dumps(list))


