# import only system from os
# from os import system, name
import os

# import sleep to show output for some
# not needed here, but useful to know: sleep(int? amount of seconds)
from time import sleep


# define the clear function
def clear():
    # clearing screen will not work for whatever reason
    # also, I am unable to block comment with keyboard shortcuts

    """
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    """


    # the underscore will hold the returned value of the clear screen command

    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
        print("Windows command used")
    # for mac and linux
    else:
        print("other command used")
        _ = os.system("clear")
    return _

finished = False
found = False

print()  # print blank line
print(" Welcome ot the birthday dictionary")
print(" ----------------------------------")
print()

while not finished:

    # Input dictionary from birthdays.txt
    file = open("birthdays.txt", "r")  # Opens file for reading, requires an f.close() after reading is done
    # Alternatively, you could use a "with, as" statement, where the file is auto closed

    # Declare dictionary
    d = {}
    for line in file:
        x = line.split(",")  # x is assigned a list of values that are separated by commas

        a = x[0]  # first string in line (the key)
        b = x[1]  # second string in line (the value)

        c = len(b) - 1  # counts the number of characters in the value that aren't '\n'
        b = b[0:c]  # b is reassigned without the '\n'

        d[a] = b  # dictionary at key a is assigned the value b
        # loop should repeat for remaining lines

    keys_list = d.keys()  # .keys() returns a list of its keys

    print("We know the following people:")

    # Print the keys
    for k in keys_list:
        print(k)

    # user inputs desired name
    print()
    search = input("Whose birthday do you want to look up?\n")

    # lineary search
    for k in keys_list:  # step through the keys
        if k == search:  # if the current key is the desired key
            if k[len(k) - 1] == 's':  # if the last letter of the name is s
                print(k + "' birthday is " + d[k])
            else:  # if the last letter of the name is not an s
                print(k + "'s birthday is " + d[k])  # print the dictionary value for key, k
            found = True  # found flag is set to true
            break  # no reason to continue the loop if the key has been found

    if not found:
        print("Birthday not found!")
        print("Check spelling of person")

    valid_choice_1 = False

    while not valid_choice_1:
        print()  # print blank line
        print("Would you like to search again?")
        print(" [Y] Yes")
        print(" [N] No")
        again = input()
        again = again.upper()  # converts the string (y or n) to uppercase for simple checking and reasigns it

        if again == 'N':
            finished = True
            valid_choice_1 = True
            print(" Program terminated")
        elif again == 'Y':
            finished = False
            valid_choice_1 = True
            clear()
        else:
            print("Invalid input, try again")

file.close()