#! /usr/bin/python3
import os
import subprocess

def get_files(dir):
    #Function to get the list of all files in a given directory and its subdirectories
    for root, directories, files in os.walk(dir):
        for filename in files:

            file_path = os.path.join(root, filename)
            print (file_path)

def countFiles(dir, counter = 0):
    #Function to return the number of files in a given directory and subdirectories
    for pack in os.walk(dir):
        for f in pack[2]:
            counter += 1
    return "Number of files in the directory: " + dir + ":" + str(counter)

def findPermissions(dir):
    #Function to find the permissions of all files in a given directory
    for root, directories, files in os.walk(dir):
        for filename in files:
            #This combines the two strings to get the full file path
            filepath = os.path.join(root, filename)
            #Gets that status of every file in the directory
            status = os.stat(filepath)
            #This prints the file permissions of all files in the directory
            print("File Permissions: " + filepath + " is: ",oct(status.st_mode)[-3:])

user_input = input("Do you want to play the game?")

if user_input in ('YES', 'Yes', 'yes', 'yeah', 'Yeah', 'y', 'Y'):
    user_input = 'True'

#This returns the current working directory
currdir = os.getcwd()

while user_input == 'True':
    print("Please choose one of the options listed below: ")
    print("1. List the files present in a given directory and all subdirectories")
    print("2. Find the total number of files in a given directory and all subdirectories")
    print("3. Find the permissions of each file in the given directory and all subdirectories")
    print("4. Change the permissions of a given file")

    user_selection = input("Please select an option: ")
    
   

    if user_selection == '1': 

        testdir = input("Please enter the full path of the directory you want to list the files of: ")

        if testdir == '':
            testdir = currdir
            print("You did not enter any value, using the current directory to list files")

            get_files(testdir)

        elif not os.path.isdir(testdir):
            print(testdir, 'This folder could not be found.')

        else:
            get_files(testdir)




    elif user_selection == '2':
        testdir = input("Please enter the full path of the directory to find the file count of: ")
        if not os.path.isdir(testdir):
            print(testdir, 'This folder could not be found.')
        elif testdir == '':
            testdir = currdir
            print("You did not enter any value, using the current directory to list file count")
        print(countFiles(testdir))
   

   elif user_selection == '3':
        testdir = input("Please enter the directory in which you want to find the permissions of all files in: ")
        if not os.path.isdir(testdir):
            print(testdir, 'This folder could not be found.')
        elif testdir == '':
            testdir = currdir
            print("You did not enter any value, using the current directory to list file count")
        print(findPermissions(testdir))
   


   elif user_selection == '4':
        testFile = input("Please enter the file name (including the fullpath) that you want to change the permissions of: ")
        if not os.path.isfile(testFile):
            print(testFile, 'This file could not be found.')
        else:
            status = os.stat(testFile)
            print("Current File Permissions of " + testFile + " are",oct(status.st_mode)[-3:])
            new_Perm = str(input("Please enter the new permissions you want to apply in octal form: ex.: 777: "))
            os.chmod(testFile, int(new_Perm, 8))
            status = os.stat(testFile)
            print("New File Permissions of " + testFile + " are",oct(status.st_mode)[-3:])
            subprocess.call(["ls","-l",testFile])
    else:
         print("Not a valid selection")
    user_input = input("Do you want to continue?")
    if user_input in ('YES', 'Yes', 'yes', 'yeah', 'Yeah', 'y', 'Y'):
        user_input = 'True'
    else:
        print("Thank you for playing the game")

        



