import os.path
import os
import json
from getInput import *

def createFile(filename, text):
    try:
        f = open(filename, "x")
        f.write(text)
        f.close()
        return True
    except:
        print("Failed to create file")
        return False

def readFile(filename):
    if os.path.exists(filename):
        f = open(filename, "r")
        return f.read()
    else:
        print("File does not exist")
        return ""

def storeArray(array, filename):
    success = False
    if os.path.exists(filename) == True:
        #overwrite
        result = askQuestion_YorN("Do you wish to overwrite storage file? (Y/N) ")
        if result == "y":
            os.remove(filename)
            text = ','.join(str(e) for e in array)
            createFile(filename, text)
        else:
            return False
    else:
        #create
        text = ','.join(str(e) for e in array)
        createFile(filename, text)
    return True

def readArray(filename):
    file = readFile(filename)
    array = file.split(",")
    return array

def storeJSON(dict, filename):
    if os.path.exists(filename) == True:
        # Overwrite
        result = askQuestion_YorN("Do you wish to overwrite storage file? (Y/N) ")
        if result == "y":
            os.remove(filename)
            text = json.dumps(dict)
            createFile(filename, text)
        else:
            return False
    else:
        # Create
        text = json.dumps(dict)
        createFile(filename, text)

def readJSON(filename):
    file = readFile(filename)
    dict = json.load(file)
    return dict