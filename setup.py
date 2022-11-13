import shutil
from subprocess import Popen, PIPE
process = Popen('python --version', stdout=PIPE, stderr=None, shell=True)
output = process.communicate()[0]
if 'python' in output:
    print('You need to install python')
    quit()



#Move it to the desktop in order
shutil.move('./project_folder/lauch.bat', '“path/to/Desktop”')
shutil.move('./project_folder', 'path/to/Desktop')


