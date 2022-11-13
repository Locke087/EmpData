import shutil
from subprocess import Popen, PIPE
#THIS is not working, need to fix and basically copy and pasted from the code
#TODO get python version


#TODO: Move the bat file here  to the desktop in folder
shutil.move('./project_folder/lauch.bat', '“path/to/Desktop”')
#TODO: Move all theproject folder to desktop folder
shutil.move('./project_folder', 'path/to/Desktop')


