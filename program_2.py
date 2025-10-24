# Title: Word Separator
# Author: Dalila Spencer
# Date: 2025-10-23

# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def word_separator(sentence):

    new_sentence = ''

    for word in sentence:

        if word.isupper():
            new_sentence += ' ' + word

        else:
            new_sentence += word

    new_sentence = new_sentence.lower().strip()
    new_sentence = new_sentence[0].upper() + new_sentence[1:]

    new_sentence = (f'{new_sentence}.')

        #    Add your logic here)

    return new_sentence.strip()

# Example usage

#sentence = "StopAndSmellTheRoses"

sentence = input('Enter a sentence with no spaces and first letter of each word capitalized: ')

new_sentence = word_separator(sentence)

print(new_sentence)