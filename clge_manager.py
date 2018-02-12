import os
from clge import ProjectCreator
import sys
from clge import PluginInstaller, UninstallPlugin, GetPlugins, list

if __name__ == '__main__':
    print("Welcome to CLGE Project Creator")
    if len(sys.argv) == 2:
        ProjectCreator(sys.argv[1])
        print("Your Project is created")
    elif len(sys.argv) == 3:
        if sys.argv[1] == "install":
            PluginInstaller(os.path.dirname(__file__) + "/" + sys.argv[2] + ".zip", sys.argv[2])
            print("Plugin is installed")
        else:
            print("Unknown command")
            raise SystemExit
    else:
        inp = input("Command: (Skip if you want to create a project): ")
        if inp == "install":
            pn = input("Plugin name (Without .zip): ")
            PluginInstaller(os.path.dirname(__file__) + "/" + pn + ".zip", pn)
            print("Plugin is installed")
        elif inp == "uninstall":
            pn = input("Plugin name: ")
            UninstallPlugin(pn)
            print("Plugin is uninstalled successfully")
        elif inp == "plugins":
            print("Installed plugins: {}".format(GetPlugins(list)))
        else:
            projname = input("Project Name: ")
            ProjectCreator(projname)
            print("Your Project is created")
