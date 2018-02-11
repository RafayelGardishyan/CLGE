import sys
from .exceptions import CLGEException

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

if get_platform() == "OS X":
    packages_list = ['pyobjc-core', 'pyobjc', 'pyautogui ', 'coverage', 'keyboard', 'mouse', 'playsound', 'colored', 'multitasking']
elif get_platform() == "Linux":
    packages_list = ['xlib', 'pyautogui ', 'coverage', 'keyboard', 'mouse', 'playsound', 'colored', 'multitasking']
else:
    packages_list = ['pyautogui ', 'coverage', 'keyboard', 'mouse', 'playsound', 'colored', 'multitasking']


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