# Title: Capital Quiz
# Author: Dalila Spencer
# Date: 2025-10-23

# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).

import random

statesAndCapitals = {'Alabama':'Montgomery', 'Alaska':'Juneau','Arizona':'Phoenix', 'Arkansas':'Little Rock',
                       'California':'Sacramento', 'Colorado':'Denver', 'Connecticut':'Hartford', 'Delaware':'Dover',
                       'Florida':'Tallahassee', 'Georgia':'Atlanta', 'Hawaii':'Honolulu', 'Idaho':'Boise',
                       'Illinois':'Springfield', 'Indiana':'Indianapolis', 'Iowa':'Des Moines', 'Kansas':'Topeka',
                       'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge', 'Maine':'Augusta', 'Maryland':'Annapolis',
                       'Massachusetts':'Boston', 'Michigan':'Lansing', 'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                       'Missouri':'Jefferson City', 'Montana':'Helena', 'Nebraska':'Lincoln', 'Nevada':'Carson City',
                       'New Hampshire':'Concord', 'New Jersey':'Trenton', 'New Mexico':'Santa Fe', 'New York':'Albany',
                       'North Carolina':'Raleigh', 'North Dakota':'Bismarck', 'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                       'Oregon':'Salem', 'Pennsylvania':'Harrisburg', 'Rhode Island':'Providence', 'South Carolina':'Columbia',
                       'South Dakota':'Pierre', 'Tennessee':'Nashville', 'Texas':'Austin', 'Utah':'Salt Lake City',
                       'Vermont':'Montpelier', 'Virginia':'Richmond', 'Washington':'Olympia', 'West Virginia':'Charleston',
                       'Wisconsin':'Madison', 'Wyoming':'Cheyenne',}

states = list(statesAndCapitals.keys())
repeat = 'y'

print('You will be give the names of different states.')
print('Please enter the capital for each state.')
print('Make sure you answer is spelled correctly and every word it spelled out and capitalized.')


while repeat == 'y':
    count = 49
    correct = 0

    random.shuffle(states)

    for state in states:

        response = input(f'What is the capital of {state}?: ')
        if response.strip() == statesAndCapitals.get(state):
            print('Correct!')
            correct += 1
        else:
            print('Incorrect!')
            print(f'The correct answer was {statesAndCapitals.get(state)}.')

    print(f'You answered {correct} out of 50 correctly')
    print(f'You answered {50 - correct} out of 50 incorrectly')

    repeat = input('Would you like to try again? y/n: ')
    repeat = repeat.lower()


