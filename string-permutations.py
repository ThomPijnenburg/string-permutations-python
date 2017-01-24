# This little program asks the user for a word and returns all its permutations

from math import *
import sys

# This is the main part of the program
def main():
    # Ask the user for a word for which to return its permutations
    word = input("Please enter the word you want permuted: ")
    # Use the permute function on this word
    permutations = permute(word)

    # permutations is a list of lists of letters, for readability concatenate inner lists
    formatted_permutations = []
    for p in permutations:
        formatted_permutations.append(''.join(p))

    # print results
    print(formatted_permutations)

    # Check if number of found permutations corresponds to the mathematically
    # predicted value: word with length n has n! permutations
    perms_number = len(permutations)
    print('Number of permutations: %d' %(perms_number))

    # Print mathematically predicted value, correct for the situation where the word
    # is empty since 0!= 1
    if len(word) !=0:
        pred_length = factorial(len(word))
    else:
        pred_length = 0
    print('Expected number: %d' %(pred_length))

# This function calculates all permutations of a word
def permute(word):
    # separate word into individual letters
    letters = list(word)
    # we will store resul in here
    result = []

    # if there are no letters in the word, return empty list
    if len(letters) ==0:
        print('Your given word is empty')
        return result

    # if the word is a single character, return that single character
    if len(letters) == 1:
        result.append(word)
        return result

    # iterate over all characters of the word
    for i in range(len(letters)):
        # use letters[i] as the first character of the permutation
        letter = letters[i]
        # extract this from the remaining characters
        remainder = letters[:i] + letters[i+1:]

        # construct all permutations for which 'letter' was the starting character
        for p in permute(remainder):
            result.append([letter] + p)
    return result

if __name__ == '__main__':
    sys.exit(main())
