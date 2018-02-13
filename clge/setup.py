import sys
import os
from .exceptions import CLGEException
# import configparser
import json

def get_packages():
    try:
        return json.loads(open(os.path.dirname(os.path.realpath(__file__)) + "/packages.json").read())
    except:
        return json.loads(open(os.path.dirname(os.path.realpath(__file__)) + "packages.json").read())

def get_platform():
    platforms = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'darwin': 'OS X',
        'win32': 'Windows',
        'uwp': 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]


packages = get_packages()


if get_platform() == "OS X":
    packages_list = packages["OS X"] + packages["Standard"]
elif get_platform() == "Linux":
    packages_list = packages["Linux"] + packages["Standard"]
else:
    packages_list = packages["Windows"] + packages["Standard"]


def packages_list_string():
    output = ""
    for package in packages_list:
        output += package + " "
    return output

try:
    import pip
    for package in packages_list:
        try:
            pip.main(['install', package])
        except:
            raise CLGEException("Unable to install {}".format(package))
    print("\n"*100)
except ImportError:
    print("Error: No pip module. Can't do setup")
    print("Info: Please install the packages manually")
    print("Info: Package List: {}".format(packages_list_string()))
    raise SystemExit


# def get_config_data(config_file):
#     config = configparser.ConfigParser()
#     config.read(config_file)
#     return config
