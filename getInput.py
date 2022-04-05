def askQuestion_string(question):
    return str(input(question))

def askQuestion_integer(question):
    try:
        answer = int(askQuestion_string(question))
    except:
        print("I didn't understand the integer you entered.")
        answer = False
    return answer

def askQuestion_float(question):
    try:
        answer = float(askQuestion_string(question))
    except:
        print("I didn't understand the float you entered.")
        answer = False
    return answer

def askQuestion_YorN(question):
    result = False
    while result == False:
        result = askQuestion_string(question).lower()
        if result != "y" and result != "n":
            print("Valid answers are either Y or N please type clearly.")
    return result
            
