import sys
packages_list = ['keyboard', 'playsound', 'colored', 'multitasking']

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
            print("Unable to install {}".format(package))
            raise SystemExit
except ImportError:
    print("Error: No pip module. Can't do setup")
    print("Info: Please install the packages manually")
    print("Info: Package List: {}".format(packages_list_string()))
    raise SystemExit

def get_platform():
    platforms = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'darwin': 'OS X',
        'win32': 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]