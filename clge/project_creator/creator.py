import os
import errno
import shutil
from ..exceptions import CLGEException

def start_project(directory):
    """
    Function which creates a project folder
    :param directory: Project folder
    :return: None
    """
    try:
        os.makedirs(directory)
        os.makedirs(directory + "/clge")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise CLGEException("Project Folder Already Exists")
        else:
            raise CLGEException("Could not create Project Folder")

def copy_engine(directory, symlinks=False, ignore=None):
    """
    Function which copies the main CLGE folder to the project folder
    :param directory: Project directory
    :param symlinks: Symlinks (See shutil.copytree documentation)
    :param ignore: Ignor (See shutil.copytree documentation)
    :return: None
    """
    for item in os.listdir("./clge"):
        s = os.path.join("./clge", item)
        d = os.path.join(directory + "/clge", item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def copy_sample_project(directory, symlinks=False, ignore=None):
    """
    UserDefinedFunctionManager which copies the sample project files to the project folder
    :param directory: Project directory
    :param symlinks: Symlinks (See shutil.copytree documentation)
    :param ignore: Ignor (See shutil.copytree documentation)
    :return: None
    """
    for item in os.listdir("./clge/project_creator_files"):
        s = os.path.join("./clge/project_creator_files", item)
        d = os.path.join(directory, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def ProjectCreator(project_name):
    """
    Frunction which creates the project
    :param project_name: Project name -> Directory name
    :return: None
    """
    start_project(project_name)
    copy_engine(project_name)
    copy_sample_project(project_name)
