"""
    AUTHOR: JEAN PAUL T. SAN GABRIEL
"""
def main():
    start = None
    end = None
    # Ask user to enter the start range. Repeat asking until user enters a valid number
    while not start:
        try:
            start = int(input('From what number would you like to process? '))
        except:
            print('Invalid input.')

    # Ask user to enter the end range. Repeat asking until user enters a valid number
    # The number must be higher than the first number entered.
    while not end:
        try:
            end = int(input('Up to what number would you like to process? '))
            if end < start:
                print('You must enter a number greater than or equal to %d' % start)
                end = None
                continue
        except:
            print('Invalid input.')

    # Store odd numbers in a list using list comprehension. Zero is neither odd or even.
    odd = [str(n) for n in range(start, end + 1) if n % 2 == 1 and n != 0]

    # Store even numbers in a list using list comprehension. Zero is neither odd or even.
    even = [str(n) for n in range(start, end + 1) if n % 2 == 0 and n != 0]

    # Display the results to the screen
    print('\nThere are %d Odd numbers:' % len(odd), ' '.join(odd))
    print('There are %d Even numbers:' % len(even), ' '.join(even))
    input('\nPress enter to continue.')
