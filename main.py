# This program generates a password that consists 3 letters, 6 numbers and 1 speical character.
# Written by: Thu Aung
# Written on: Sept 12, 2020

# Import string and random for getting random alphabets and numbers + shuffling.
import string
import random

# Create empty list to hold all alphabets, numbers and a special character as strings.
pwd_list = []
# Create empty string for later joining strings in list.
pwd = ''

# Get 3 random letters from alphabets and add them to list.
def mixed_letter():
    letter = list(string.ascii_lowercase)
    random.shuffle(letter)
    # For heightened security, make one letter upper case.
    first_letter = letter[0].upper()
    pwd_list.append(first_letter)
    pwd_list.append(letter[1])
    pwd_list.append(letter[2])

# Using while loop, get 6 random numbers and add them to list.
def mixed_num():
    i = 0
    while i < 6:
        num = random.randint(0,9)
        # Change int to str for later using in join().
        num = str(num)
        pwd_list.append(num)
        i+=1

# Get 1 random special character and add to list.
def mixed_char():
    # First, create a list of special characters as a string.
    char_list = ["!", "@", "#", "%","$", "&","*"]
    random.shuffle(char_list)
    char = char_list[0]
    pwd_list.append(char)

# Shuffle the list.
def mixed_list():
    return random.shuffle(pwd_list)

# Join strings for final password.
def pwd():
    return ''.join(pwd_list)

mixed_letter()
mixed_num()
mixed_char()
mixed_list()
print('You new password is: ', pwd())
print("Thank you for choosing to use this program.")