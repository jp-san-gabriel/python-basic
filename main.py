"""
    AUTHOR: JEAN PAUL T. SAN GABRIEL
"""
from exercises import payroll, quiz, rock_paper_scissors, odd_even

modules = [
    { 'title': 'Payroll', 'module':payroll },
    { 'title': 'Odd Even Processor', 'module': odd_even },
    { 'title': 'Games', 'module': [
        { 'title': 'Quiz Game', 'module': quiz },
        { 'title': 'Rock, Paper, Scissors', 'module':rock_paper_scissors }
    ]}
]

def executeModules(modules, subModule = False, title = 'Welcome to Our Portal'):
    """
        This function allows user to recursively traverse a list of modules that
        may contain sub-modules.
        Each item in the 'modules' list is a dictionary that has the following keys:
            title - A string containing the title of the module
            module - the module itself is assigned to this key

        Each module has a main() function which is called when the user selects
        the module.  If the module key contains a list, it is treated as a
        sub-module.  This function, recursively executes taking the list as input
        for its parameter 'modules'.
    """
    while True:
        # Print the title
        print('\n%s\n' % title.center(30, '-'))

        # Displays the list of modules
        for index, module in enumerate(modules, 1):
            print('%d - %s' % (index, module['title']))

        # If we are in a sub-module, display 'Previous Menu' as the
        # last option instead of 'Exit'
        if subModule:
            print('b - Previous Menu')
        else:
            print('x - Exit')

        # Prompt the user to enter its choice, converting its input to lowercase
        choice = input('\nEnter option: ').lower()

        # If user enters 'x' and we are not in a sub-module, display Thank you and break the loop
        if choice == 'x' and not subModule:
            print('Thank you!')
            break

        # If user enters 'b' and we are in a sub-module, simply break the loop
        elif choice == 'b' and subModule:
            break
        else:
            try:
                # Get the selected module from the 'modules' list
                selectedModule = modules[int(choice) - 1]

                # if the datatype of the 'module' attribute of the selectedModule
                # is a list, treat it as a sub-module. Recursively call this
                # function treating the list as sub-modules.
                if type(selectedModule['module']) is list:
                    executeModules(selectedModule['module'], subModule = True, title = selectedModule['title'])
                else:
                    # The datatype of the 'module' attribute is not list. Simply execute its main() function
                    selectedModule['module'].main()
            except:
                # User enters an invalid input. Prompt him/her to press enter to continue.
                input('Invalid input. Press enter to continue.')

# call the function
executeModules(modules)
