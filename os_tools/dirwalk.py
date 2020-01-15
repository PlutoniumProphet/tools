"""Simple directory walk - prints content of 'projects' directory to console"""
import os

os.chdir("/Users/grahamkesley/projects/")

for root, dirs, files in os.walk(".", topdown=False):
    print("In folder: " + root)
    for name in dirs:
        print("Directories: " + os.path.join(root, name))
    for name in files:
        print("Files: " + os.path.join(root, name))
    print("---------\n")
