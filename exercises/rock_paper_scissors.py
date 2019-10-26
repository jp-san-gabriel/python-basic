"""
    AUTHOR: JEAN PAUL T. SAN GABRIEL
"""
from random import randint

def main():
    # Create an array containing the strings 'Rock', 'Paper', 'Scissors'
    weapons = 'Rock Paper Scissors'.split()

    # Construct the string that displays the options
    selectionString = '\n' + ', '.join(['[%d] %s' % (index, weapon) for index, weapon in enumerate(weapons, start = 1)])


    while True:
        # get user's selection. Repeat until user enters a valid input
        try:
            userSelectedWeapon = int(input('%s\nChoose your weapon: ' % selectionString)) - 1
            if userSelectedWeapon not in range(0, 3):
                raise Exception()
        except:
            input('Invalid input. Press enter to continue')
            continue

        # Generate computer's selection
        computerSelectedWeapon = randint(0, 2)
        print('Computer chose %s' % weapons[computerSelectedWeapon])

        # Compute result.
        difference = userSelectedWeapon - computerSelectedWeapon

        # If the difference of user selected index minus computer selected index
        # is either 1 or -2, the user wins
        if difference in (1, -2):
            print('You win!')
        # If the difference is 0, it's a draw
        elif difference == 0:
            print('Draw!')
        # Otherwise, the user looses.
        else:
            print('You lost!')

        # Prompt user to play again. Repeat asking until user's input is valid
        while True:
            playAgain = input('\nPlay Again? (y/n):').lower().strip()
            if playAgain not in 'yn':
                input('Invalid input. Press enter to continue.')
                continue
            break

        # If user selected No, break the outer loop
        if playAgain == 'n':
            break
