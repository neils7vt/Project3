#! /bin/usr/python3
import os

user_input = input("Do you want to play the game?")

if user_input in ('YES', 'Yes', 'yes', 'yeah', 'Yeah', 'y', 'Y'):
    user_option = 'True'

while user_option == 'True':
    print("Please choose one of the options listed below: ")
    print("1. List the files present in a given directory and all subdirectories")
    print("2. Find the total number of files in a given directory and all subdirectories")


    user_selection = input("Please select an option: ")



