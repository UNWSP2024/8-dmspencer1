# Title: Initials
# Author: Dalila Spencer
# Date: 2025-10-23

# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names, 
# and displays their first, middle, and last initials.  
# For example, if the user enters John William Smith, the program should display J. W. S.

# Add your logic starting on line 11

def initials_generator(personsName):

    try:
        Namelist = personsName.split()

        personsInitials = f"{Namelist[0][0]}.{Namelist[1][0]}.{Namelist[2][0]}."

    except IndexError:
        return 'Invalid input'

    return personsInitials.strip()

personsName = input('Enter the users first, middle, and last name: ')

initials = initials_generator(personsName)

print(initials.upper())