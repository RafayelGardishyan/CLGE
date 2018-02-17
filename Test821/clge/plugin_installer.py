import os
import json
from .exceptions import CLGEException
import zipfile
import os
import shutil

path = os.path.dirname(__file__)


def GetPlugins():
    PluginList = json.load(open(path + "/plugs/plugs.json"))
    plugins = ""
    for plugin in PluginList:
        plugins += plugin + " "
    return plugins


def UninstallPlugin(plugin_name):
    shutil.rmtree(path + r"/plugs/" + plugin_name)
    PluginList = json.load(open(path + "/plugs/plugs.json"))
    PluginList.pop(PluginList.index(plugin_name))
    open(path + "/plugs/plugs.json", "w+").write(json.dumps(PluginList))


def PluginInstaller(plugin_full_path, plugin_name):
    with zipfile.ZipFile(plugin_full_path, "r") as z:
        os.makedirs(path + r"/plugs/" + plugin_name)
        z.extractall(path + r"/plugs/" + plugin_name)
        PluginList = json.load(open(path + "/plugs/plugs.json"))
        PluginList.append(plugin_name)
        plugins = GetPlugins()
        print("Your installed plugins: {}".format(plugins))
        open(path + "/plugs/plugs.json", "w+").write(json.dumps(PluginList))


