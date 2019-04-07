# Python 3.6.3 Scripting Examples by Rich K for Task 29842
# Note a lot of this is similar in Python 2, but not the same
# Remember, Ctrl+Z then Enter to exit a command line python session in Windows

# Console Write
print ("*************Console Write*************")
print ("This is print() console output, which will have a new line")
pi = 3.15927
print ("The number pi is about: ", str(pi))
print (f"Here is pi produced by formatted literals: {pi}")
print ("Here is pi to two places with str.format(): {:.3}".format(pi))

# Debug Output
import logging, sys
print ("*************Debug Output*************")
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logging.debug("A debug message!")

# Keyboard Input
print ("*************Keyboard Input*************")
name = input("Enter a name: ")
print (f"Hello \"{name}\"")

# Command-line Args
import sys, ntpath
print ("*************Command-line Args*************")
print ("This is the name of the script: ", ntpath.basename(sys.argv[0]))
print ("Number of arguments: ", len(sys.argv))
print ("The arguments are: " , str(sys.argv))

# Registry Actions
from winreg import *
print ("*************Registry Actions*************")
"""print r"*** Reading from SOFTWARE\Microsoft\Windows\CurrentVersion\Run ***" """
aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
aKey = OpenKey(aReg, r"SOFTWARE\WOW6432Node\Psychology Software Tools\E-Prime\3.0\E-Studio\Packages\SearchFolders")
firstPackageFolder = "(unknown)"
firstPackageFolder = QueryValueEx(aKey, "Folder1")
print (f"Package Search Folder1 \"{firstPackageFolder}\"")

# Folder/File Found (notice I use generic "os" instead of ntpath this time)
import os
print ("*************Folder/File Found*************") 
print ("Parent folder", "exists" if os.path.isdir(os.path.dirname(sys.argv[0])) else "doesn't exist")
print ("This .py file", "exists" if os.path.exists(sys.argv[0]) else "doesn't exist")

