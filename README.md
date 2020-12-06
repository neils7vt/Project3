# Project3

# My program is a game that allows the user to perform a set of Linux Administration and search within file tasks based on their selection out of 8 options.
# 
# Due to the simple nature of my initial project proposal of searching a file for words/sentences, I added 7 more options to my project to better cover several Linux               Administation tasks and use more linux os commands in python code.
# I run my program using the following: python3 Project3.py, or: python3 /fullpath/Project3.py
#
# A message is displayed to the user: "Do you want to play the game?" Enter yes to play (multiple user input variations covered), or no if not (program ends).
#
# A menu of options is displayed to the user, enter in just the number of the option to select one.
#
# Options:
#
# 1. List all the files of a directory and its subdirectories. Requires a full path. Ex: home/neils7/projects
#    Cases: No entry given (just enter pressed): List the files of the current working directory and all subdirectories
#           Invalid directory: Message indicating invalid directory and prompt user if they want to continue the game. If "yes" is entered, display menu of options again. 
#
# 2. Find the number of files in a directory and all its subdirectories. Requires a full path. Ex:home/neils7/projects
#    Cases: No entry given (just enter pressed): Count the number of files in the current working directory and all subdirectories, display to user the count.
#           Invalid directory: Message indicating invalid directory and prompt user if they want to continue the game. If "yes" is entered, display menu of options again. 
#
# 3. Find the permissions of all files in a directory and all its subdirectories. Lists permissions of all files in a list, using their 3-digit permissions value. Requires a          full path. Ex: home/neils7/projects
#    Cases: No entry (just enter pressed): Finds the permissions of the files in the current working directory and all subdirectories.
#           Invalid directory: Message indicating invalid directory and prompt user if they want to continue the game. If "yes" is entered, display menu of options again. 
#
# 4. Change the permissions of a file. User is asked for the file they wish to change the permissions of (if file is not in current directory, enter full path ex: /home/neils7/file1.txt ). If the file is in the current directory, simply type the file name (file1.txt). The current permissions of the file are displayed. Then, user is asked to enter the 3-digit code for the new permissions of the file ex: '777'. After changing the files permissions, the file and its new permissions are listed.
#    Cases: No entry (prompt for file): Display error message and ask user if they want to continue the game.
#           Invalid file (prompt for file) (file not found): Message indicating invalid file and prompt user if they want to continue the game. If "yes" is entered, display menu of options again. 

# 5. Search for a user-inputed word in a given file. User is asked to enter a word to search for, followed by a space, and then the full path of the file to search for the word     in (ex: print /home/neils7/Project3.py). If the file is in the current directory, simply enter the file name with the extension rather than the full path. The total number       of occurences of the word is displayed as well as the list of lines that contain the given word.
#    Cases: Invalid file (file not found): Message indicating invalid file and prompt user if they want to continue the game.

# 6. Rename a file. The user is asked to give the name of the file they wish to rename, followed by a space, followed by the new file name. (include extension). Full path of          both file names is required if not in current directory. New file name is displayed.
#    Cases: Invalid file (file not found): Message indicating invalid file and prompt user if they want to continue the game.
#
# 7. Find the number of files with a given extensions type in a directory and all its subdirectories. The user is first asked to give the full path of the directory to search        in. Then, they are prompted to give the extension type they want to search for (ex: .txt). The total number of files with given extension type in each directory is listed.
#    Cases: No entry (just enter pressed) for directory prompt: Search in current directory
#           Invalid directory: Message indicating invalid directory and prompt user if they want to continue the game. If "yes" is entered, display menu of options again. 
#
#
# 8. Find the number of files greater than a user-inputed size in bytes in a directory and all its subdirectories. The user is asked to give the full path of the directory to        search within. Then, the user is asked to enter the file size in bytes that they wish to search for files greater than (ex: 100). All files that meet the requirement are        listed and their file size is displayed.
#    Cases: No entry (just enter pressed) for directory prompt: Search in current directory
#           Invalid directory: Message indicating invalid directory and prompt user if they want to continue the game. If "yes" is entered, display menu of options again. 
#
#
# For any "continue prompt" case, if anything other than 'yes', 'y', 'Y', 'Yeah', 'yeah', or 'YES' is entered, a thank you message is displayed to the terminal and the program ends.

