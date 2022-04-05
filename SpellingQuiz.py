from .getInput import *
import random
# Spelling Quiz
quiz = [
    ["What structure do people occupy? ", "building"], 
    ["What animal makes the noise MOO? ", "cow"]
    ]

def compareSpelling(attempt, actual):
    listAttempt = list(attempt)
    listActual = list(actual)
    for i in range(len(actual)):
        if listAttempt[i] == listActual[i]:
            #output.join(actual[i:1])
            j=0
        else:
            listActual[i] = "_"
    output = "".join(listActual)
    return output

def checkMisspelling(word):
    for x in range(len(word)):
        if word[x:1] == '_':
            return False
    return True

def SpellingQuiz():
    leave = False
    while leave == False:
        index = random.randint(0,len(quiz)-1)
        answer = quiz[index][1].lower()
        next = False
        while next == False:
            guess = askQuestion_string(quiz[index][0]).lower()
            if guess == "leave":
                leave = True
            incorrect = compareSpelling(guess, answer)
            if checkMisspelling(incorrect) == False:
                print("The word you entered does not match my answer")
                print("This is what I understood {0}".format(incorrect))
            else:
                print("Wonderful spelling. Well done")
                next = True

SpellingQuiz()
