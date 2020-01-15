"""Simple directory walk - prints content of 'projects' directory to console"""
import os

os.chdir("/Users/grahamkesley/projects/")

class Bcolors:
    """ANSI colours for terminal printing"""
    DIRECTORIES = '\033[95m'
    FILES = '\033[94m'
    LABELS = '\033[93m'
    ENDC = '\033[0m'


for root, dirs, files in os.walk(".", topdown=False):
    print(Bcolors.LABELS + "In folder: " + root + Bcolors.ENDC)
    for name in dirs:
        print(Bcolors.DIRECTORIES + "Directories: " + Bcolors.ENDC
              + os.path.join(root, name))
    for name in files:
        print(Bcolors.FILES + "Files: " + Bcolors.ENDC
              + os.path.join(root, name))
    print("---------\n")
