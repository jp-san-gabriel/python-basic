"""
    AUTHOR: JEAN PAUL T. SAN GABRIEL
"""
from random import randint
from json import load

def quiz(questions):
    # put questions in a temporary list:
    unansweredQuestions = list(questions)

    # initialize counter for correct answers:
    totalScore = 0

    # Repeat the following 10 times:
    for i in range(10):

        # Randomly get a question from the list, removing it from the list
        question = unansweredQuestions.pop(randint(0, len(unansweredQuestions) -1))

        # Display the question
        print('\nQ%d:' % (i + 1), question['question'], '(%d points)' % question['score'])

        # Loop for 3 times:
        for j in range(3):
            # Prompt user for an answer
            answer = input('Answer:')

            # If answer is right, terminate the loop
            isCorrectAnswer = answer.strip().lower() == question['answer'].strip().lower()
            if isCorrectAnswer:
                totalScore += question['score']
                print('Correct!\nTotal Score: %d' % totalScore)
                break
            else:
                # otherwise, tell user that his/her answer is wrong
                print('Incorrect. Please try again. (Remaining attempts: %d)' % (2 - j))

        # If user did not get the correct answer, display the correct answer
        if not isCorrectAnswer:
            print('\nThe correct answer is "%s"' % question['answer'])

    return totalScore


# This function displays the scores
def displayScores(scores):
    print('\n{:=^40}'.format(' Score Board '))

    # Sort the scores from highest to lowest
    sortedScores = sorted([(name, score) for name, score in scores.items()], key = lambda item: item[1], reverse = True)

    # Display the scores
    for playerName, score in sortedScores:
        print('{:.>18} : {:.<19}'.format(playerName, score))

    # Let user press enter to continue.
    input('\nPress enter to continue.')


# -------------------------------MAIN ---------------------------------------

def main():
    # Load questions from file and store it as a list of dictionariesself.
    # Questions are saved in a text file in json format.
    with open('resources/questions.txt', 'r') as file:
        questions = load(file)

    # Load scoreboard from file and put it in a dictionary
    scores = {}
    with open('data/scores.txt', 'r') as file:
        for line in file:
            scores[line[:line.rfind(':')]] = int(line[line.rfind(':') + 1:])


    while True:
        # Display the options and ask for user's choice.
        # Repeat until the user's input is valid.
        while True:
            print('\n%s' % 'Quiz Game'.center(30, '-'))
            print('\n1 - Play game\n2 - View scoreboard\nQ - quit')
            option = input('\nEnter option: ').strip().lower()
            if option not in ('1', '2', 'q'):
                print('Invalid input')
                continue
            break

        # If user selects option 1 - Play Game...
        if option == '1':
            # Start quiz, then Prompt user for name:
            scores[input('\nEnter your name: ')] = quiz(questions)

            # Save scores to a file
            with open('data/scores.txt', 'w') as file:
                for name, score in scores.items():
                    file.write("%s:%d\n" % (name, score))

        # If user selects option 2 - View scoreboard
        elif option == '2':
            # Display scores
            displayScores(scores)

        # Otherwise, quit the game by breaking the outermost loop
        else:
            break
