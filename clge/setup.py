import sys
import subprocess
import os
import json
from clge.exceptions import CLGEException

if os.geteuid() == 0:
    print("Running as root.")
else:
    raise CLGEException("You have to run CLGE with sudo to be able to use keyboard controls")

def get_packages():
    return json.loads(open(os.path.dirname(os.path.realpath(__file__)) + "/packages.json").read())


def get_platform():
    platforms = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'linux': 'Linux',
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
    for Package in packages_list:
        output += Package + " "
    return output


try:
    for package in packages_list:
        if get_platform() == "Windows":
            subprocess.check_call(["python", '-m', 'pip', 'install', package, '--user'])
        else:
            subprocess.check_call(["python3", '-m', 'pip', 'install', package, '--user'])
    print("\n" * 100)
except ImportError or subprocess.CalledProcessError:
    print("Error: No pip module. Can't do setup")
    print("Info: Please install the packages manually")
    print("Info: Package List: {}".format(packages_list_string()))
    raise SystemExit

# def get_config_data(config_file):
#     config = configparser.ConfigParser()
#     config.read(config_file)
#     return config
