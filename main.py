from cgi import print_arguments
import os
import sys
import time

from Functions.Functions import *

# The following prints just add some logs to the program
print("#", "="*50, "#\n")
print("\t\tProgramm is starting now")
print("\t      Loading Central File Manager")

File = ""
deleteFile = False
editFile = False
seeWholeFile = False
seePartFile = False

# Now the options will be displayed
while True:
    while True:
        if File == "":
            os.system("CLS")
            print("#", "="*50, "#\n")
            print("File name: File Not Loaded \n")
            print("\t\t","Options available\n")
            print("\t1. Load file\n"
                "\t2. Delete file (Unavailable)\n",
                "\t3. Edit file (Unavailable)\n",
                "\t4. Show the whole file(Unavailable)\n",
                "\t5. Dislpay one specific line(Unavailable)\n"
                "\t6. Exit the program(Unavailable)\n"
            )
        else:
            os.system("CLS")
            print("#", "="*50, "#\n")
            print("File name: ", os.path.basename(File.name))
            print("\t\t","Options available\n")
            print("\t1. Load file\n"
                "\t2. Delete file\n",
                "\t3. Edit file\n",
                "\t4. Show the whole file\n",
                "\t5. Dislpay one specific line\n",
                "\t6. Exit the program\n"
            )
    
        userInput = input("Please choose one number: ")
        print("#", "="*50, "#\n")
        time.sleep(0.4)

        if checkIsDigit(userInput):
            userInput = int(userInput)
            if userInput >= 1 and userInput <= 6:
                break

        print('\n------------------------------------------------- ')  
        print('> INPUT ERROR: Select a valid number (1,2,3,4,5,6) <')
        print('\n------------------------------------------------- ')

        time.sleep(1.5)
        os.system("CLS")

    if userInput == 1:
        os.system("CLS")
        print("#", "="*50, "#\n")
        print("\t\tOption chosen: 1. Load file")
        print("#", "="*50, "#\n")
        File = loadFileF()

    elif userInput == 2:
        if File == "":
            print("\t\tNo file was found\n")
            print("#", "="*50, "#\n")
            time.sleep(1.5)
            
        else:
            os.system("CLS")
            print("#", "="*50, "#\n")
            print("\t\tOption chosen: 2. Delete file")
            print("#", "="*50, "#\n")
            File = deleteFileF(File)
    
    elif userInput == 3:
        if File == "":
            print("\t\tNo file was found\n")
            print("#", "="*50, "#\n")
            time.sleep(1.5)
        else:
            editFileF(File)

    elif userInput == 4:
        if File =="":
            print("\t\tNo file was found\n")
            print("#", "="*50, "#\n")
            time.sleep(1.5)
        else:
            readLinesF(File)
            os.system("PAUSE")
    
    elif userInput == 5:
        if File == "":
            print("\t\tNo file was found\n")
            print("#", "="*50, "#\n")
            time.sleep(1.5)
        else:  
            readOneLineF(File)
            os.system("PAUSE")

    elif userInput == 6:
        os.system("CLS")
        print("#", "="*50, "#\n")
        print("\tExiting the program, thanks for using it! \n")
        print("#", "="*50, "#\n")
        sys.exit()