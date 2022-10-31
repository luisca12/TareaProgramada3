from msilib.schema import File
import os
import sys
import time
from xmlrpc.client import Server

# This function checks if the input is an int
def checkIsDigit(input_str):
    if input_str.strip().isdigit():
        return True
    else:
        return False

# loadFileF Function will ask the client to input a file's path.
# newFile is a required variable, to receive this variable as a parameter
# And it will return the found file or the created file
def loadFileF():
    filePath = str(input("Please input the file path: "))

    if not os.path.isfile(filePath):
        print("The path is not a file.")
    if not os.path.exists(filePath):
        print("The file does not exist. \n")
        userInput = str(input("Woud you like to create a new file? Yes/No: "))
        userInput = userInput.lower()
        if userInput == "yes":
            newFile = open(filePath, mode="a+", encoding="utf-8")
            print("File successfully loaded!\n")
            os.system("PAUSE")
            os.system("CLS")
            return newFile        
        else:
            print("File will not be created")
            os.system("PAUSE")
            os.system("CLS")
    newFile = open(filePath, mode="a+", encoding="utf-8")
    print("File successfully loaded!\n")
    os.system("PAUSE")
    os.system("CLS")  
    return newFile

# deleteFileF Function will delete the received file in the variable File
def deleteFileF(File):
    File.close()
    os.remove(File.name)
    print("#", "="*50, "#\n")
    print("\t    Deleting the file ", File.name)
    print("\t\tFile deleted successfully! \n")
    print("#", "="*50, "#\n")
    os.system("PAUSE")
    os.system("CLS")
    return ""

def editFileF(File):
    userText = "\n" + str(input(""))
    File = open(File.name, mode="a+", encoding="utf-8")
    File.write(userText)
    File.close()
    return File

# This function will print all the file content
def readLinesF(File):
    File = open(File.name, mode="r", encoding="utf-8")
    for x in File:
        print(x.strip())

# This function will print only one line the file content
def readOneLineF(File):
    File = open(File.name, mode="r", encoding="utf-8")

    # for count in enumerate(File):
    #     pass

    while True:
        print("* Only numbers are accepted *")
        contentLine = input("Please select the line you want to see: ")
        
        if checkIsDigit(contentLine):
            contentLine = int(contentLine)
            if not checkFileLine(File,int(contentLine)):
                print("This line does not exist!")
            else:
                content = File.readline()
                print(content[contentLine])
                break
        else:
            print('\n------------------------------------------------- ')  
            print('>      INPUT ERROR: Only numbers are allowed       <')
            print('\n------------------------------------------------- ')
            os.system("PAUSE")
            os.system("CLS")
    
    os.system("PAUSE")

def checkFileLine (file, countline):
    line = 0
    for line in enumerate(file):
        pass
    if line[0] + 1 < int(countline) or int(countline) <= 0:
        return False
    return True