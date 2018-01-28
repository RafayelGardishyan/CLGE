packages_list = ['keyboard', 'playsound']
try:
    import pip
    for package in packages_list:
        try:
            pip.main(['install', package])
        except:
            print("Unable to install {}".format(package))
            raise SystemExit
except ImportError:
    print("No pip module. Can't do setup")
    raise SystemExit