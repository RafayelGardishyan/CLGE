from clge import ProjectCreator
import sys

if __name__ == '__main__':
    print("Welcome to CLGE Project Creator")
    if len(sys.argv) == 2:
        ProjectCreator(sys.argv[1])
    else:
        projname = input("Project Name: ")
        ProjectCreator(projname)
    print("Your Project is created")
