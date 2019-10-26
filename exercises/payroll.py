"""
    AUTHOR: JEAN PAUL T. SAN GABRIEL
"""
from prettytable import PrettyTable
from random import randint
import locale

def main():
    # generate random data from text files

    # Load the first names from a text file into a list
    with open('resources/first-names.txt', 'r') as file:
        firstNames = [name.strip() for name in file]

    # Load surnames from a text file into a list
    with open('resources/middle-names.txt', 'r') as file:
        lastNames = [name.strip() for name in file]

    # Load designations and salaries from a text file into a list of dictionaries
    with open('resources/positions-with-salaries.txt', 'r') as file:
        designations = [{'designation': field[0], 'salary': float(field[1])} for field in [line.strip().split(':') for line in file]]

    # Determine the start id randomly
    idStart = randint(0, 989)
    employees = {}

    # Generate random employee data by randomly getting a first name
    # and a last name from the firstNames and lastNames list,
    # including their designation and salaries
    for id in range(idStart, idStart + 10):
        employees[str(id).rjust(3, '0')] = {
            'name': '{} {}'.format(firstNames.pop(randint(0, len(firstNames) - 1)),
                lastNames.pop(randint(0, len(lastNames) - 1))),
            **designations.pop(randint(0, len(designations) - 1))
        }

    # Create the table for displaying the generated data
    menu = PrettyTable()
    menu.field_names = ['ID', 'EMPLOYEE', 'DESIGNATION', 'SALARY']
    locale.setlocale(locale.LC_ALL, 'en_US.utf8')

    for id, data in employees.items():
        menu.add_row([id, data['name'], data['designation'], locale.currency(round(data['salary'], 2), grouping = True)])

    # This is the start of the main loop for the program.
    while True:
        # Display the menu in a pretty table
        print(menu)

        # Ask User for employee ID. Repeat asking until user enters a valid ID
        employee = None
        while not employee:
            try:
                employee = employees[input('Enter Employee ID: ')]
            except:
                print('Invalid employee ID.')

        # Ask user for days rendered. Repeat asking until user enters a valid input
        daysRendered = None
        while daysRendered == None:
            try:
                daysRendered = int(input('Days Rendered: '))
            except:
                print('Invalid input.')

        # Calculate the gross income: salary / 21 x days rendered
        print('Gross Income: %s' % (locale.currency(employee['salary'] / 21 * daysRendered, grouping = True)))

        # Ask user if it wants to compute again. Repeat until user enters a valid input.
        while True:
            option = input('Compute Again? (y/n): ').lower()
            if option not in 'yn':
                print('Invalid input.')
            else:
                break

        # Break the main loop if user answers no
        if option == 'n':
            break
