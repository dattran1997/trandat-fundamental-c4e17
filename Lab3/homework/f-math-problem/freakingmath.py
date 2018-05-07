from random import *

def generate_quiz():
    # Hint: Return [x, y, op, display_result]
    x = randint(0,100)
    y = randint(0,100)
    op = choice(['+','-','*','/'])
    error = randint(-1,1)

    if (op == '+'):
        result = x + y
    elif (op == '-'):
        result = x - y
    elif (op == '*'):
        result = x * y
    elif (op == '/'):
        result = x / y
    display_result = result + error
    return [x, y, op, display_result]

def check_answer(x, y, op, display_result, user_choice):
    # x, y, op, result, user_choice
    # user_choice :True,false
    if (op == '+'):
        answer = x + y
    elif (op == '-'):
        answer = x - y
    elif (op == '*'):
        answer = x * y
    elif (op == '/'):
        answer = x / y

    if (user_choice == True) and (display_result == answer ):
        return True
    elif (user_choice == False) and (display_result != answer ):
        return True
    else:
        return False
