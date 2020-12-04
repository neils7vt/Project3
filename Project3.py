#! /bin/usr/python3
import os

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


user_input = input("Do you want to play the game?")

if user_input in ('YES', 'Yes', 'yes', 'yeah', 'Yeah', 'y', 'Y'):
    user_input = 'True'

#This returns the current working directory
currdir = os.getcwd()

while user_input == 'True':
    print("Please choose one of the options listed below: ")
    print("1. List the files present in a given directory and all subdirectories")
    print("2. Find the total number of files in a given directory and all subdirectories")


    user_selection = input("Please select an option: ")
    
    if user_selection == '1': 

        testdir = input("Please enter the full path of the directory you want to list the files of: ")
        if not os.path.isdir(testdir):
            print(testdir, 'This folder could not be found.')
        elif testdir == '':
            testdir = currdir
            print("You did not enter any value, using the current directory to list files")

        get_files(testdir)
    elif user_selection == '2':
        testdir = input("Please enter the full path of the directory to find the file count of: ")
        if not os.path.isdir(testdir):
            print(testdir, 'This folder could not be found.')
        elif testdir == '':
            testdir = currdir
            print("You did not enter any value, using the current directory to list file count")
        print(countFiles(testdir))



    else:
         print("Not a valid selection")
    user_input = input("Do you want to continue?")
    if user_input in ('YES', 'Yes', 'yes', 'yeah', 'Yeah', 'y', 'Y'):
        user_input = 'True'
    else:
        print("Thank you for playing the game")

        



