"""
Programming Task #2
Create a game where the user must correctly guess a randomly generated integer between 1 and 100.
The user should be notified whether their guess was “lower” or “higher” than the target number.
Note that you will need to use the random library’s randint function.

Remember:
- Use functions to group code
- Try to have functions that only do one “thing” (e.g. print a message, validate user input, check what message to display)
- Check for invalid inputs, notifying the user and re-prompting for a valid input

HOW THE CODE WORKS: the code is split into three different functions for clarity.. The first generates the target (correct) number to be guessed, the second validates the type and value of the guess, and the third runs the game itself (using the first two helper functions).
"""

import random

def int_randomiser():  # generates the target number using the random module
    num = random.randint(1,100)
    return num

def int_validator(guess: str):  # either v
    try:  # if the guess can be converted to integer type
        if 1 <= int(guess) <= 100:  # if the guess is within the valid range
            return 'valid'
        elif int(guess) < 1 or int(guess) > 100:  # if the guess is not within the valid range
            return 'invalid'
    except TypeError as e:  # if the guess cannot be converted to integer type
        return 'invalid'

def int_guesser():
    target = int_randomiser()
    guess = input('Guess a number between 1 to 100.\n')

    while int_validator(guess) == 'invalid':  # if the guess is invalid, the user will have to re-input it
        guess = input('Guess a VALID number between 1 to 100.')
    # breaks out of the while loop when 'valid' is returned

    if int(guess) < target:
        return "Your guess was lower than the target number."
    elif int(guess) > target:
        return "Your guess was higher than the target number."
    elif int(guess) == target:
        return "Your guess was correct."

# run the game
# print statement is required, because return does not directly show the value to the user
print(int_guesser())
