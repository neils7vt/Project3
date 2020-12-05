#! /usr/bin/python3
import os
import subprocess

def get_files(dir):
    #Function to get the list of all files in a given directory and its subdirectories
    for path1, dirs, files in os.walk(dir):
        for filename in files:

            file_path = os.path.join(path1, filename)
            print (file_path)


def countFiles(dir, counter = 0):
    #Function to return the number of files in a given directory and subdirectories
    for list1 in os.walk(dir):
        for f in list1[2]:
            counter += 1
    return "Number of files in the directory: " + dir + ":" + str(counter)


def findPermissions(dir):
    #Function to find the permissions of all files in a given directory
    for path1, dirs, files in os.walk(dir):
        for filename in files:
            #This combines the two strings to get the full file path
            filepath = os.path.join(path1, filename)
            #Gets that status of every file in the directory
            status = os.stat(filepath)
            #This prints the file permissions of all files in the directory
            print("File Permissions: " + filepath + " is: ",oct(status.st_mode)[-3:])


def searchWordinFile(searchword, filename):
    #Function to find the given word in the file and return the line number and print the line
    lineNum = 0
    matches = []
    #This opens the file in read mode
    with open(filename, 'r') as readFile:
        #Reads all lines in the file one at a time
        for searchline in readFile:
            lineNum += 1
            if searchword in searchline:
            #If found, add the line number and line string to the list
                 matches.append((lineNum, searchline.rstrip()))
    return matches



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
    print("5. Search for a given word in a file")
    print("6. Rename a given file")


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
        if testdir == '':
            testdir = currdir
            print("You did not enter any value, using the current directory to list file count")
            print(countFiles(testdir))
        elif not os.path.isdir(testdir):
            print(testdir, 'This folder could not be found.')
        else:
            print(countFiles(testdir))
   

    elif user_selection == '3':
        testdir = input("Please enter the directory in which you want to find the permissions of all files in: ")
        if testdir == '':
            testdir = currdir
            print("You did not enter any value, using the current directory to list file count")
            print(findPermissions(testdir))
        elif not os.path.isdir(testdir):
            print(testdir, 'This folder could not be found.')
        else:
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
            print("New File Permissions of " + testFile + " are ",oct(status.st_mode)[-3:])
            subprocess.call(["ls","-l",testFile])



    elif user_selection == '5':
        searchWord, searchFile = input("Please enter the word you want to search for followed by a space and then file you want to search in: ").split()
        if not os.path.isfile(searchFile):
            print(searchFile, 'This file could not be found.')
        else:
            numLines = searchWordinFile(searchWord,searchFile)
            print("Total number of lines that have the given word: ",len(numLines))
            for search_words in numLines:
                print(searchWord, " appears in line number = ", search_words[0], " and Line = ", search_words[1])

        

    else:
         print("Not a valid selection")
    user_input = input("Do you want to continue?")
    if user_input in ('YES', 'Yes', 'yes', 'yeah', 'Yeah', 'y', 'Y'):
        user_input = 'True'
    else:
        print("Thank you for playing the game")

        



