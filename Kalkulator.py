def is_number(str): # checks if the input is a number
    try:
        float(str)
        return True
    except ValueError:
        return False
    
    
def convert_number(str): # converts string into float value
    result = float(str)
    return result


def ask_for_a_number(force_valid_input): # asks for a number and forces a valid input
    while True:
        userInput = input("Please type in a number: ")
        if is_number(userInput):
            return convert_number(userInput)
        else:
            if not force_valid_input:
                return None
            print("This is not a number!")


def is_valid_operator(operator): # checks if the operator is valid
    match operator:
        case '+':
            return True
        case '-':
            return True
        case '*':
            return True
        case '/':
            return True
        case _:
            return False
    

def ask_for_an_operator(force_valid_input): # asks for an operator and forces a valid input
    while True:
        userInput = input("Please provide an operator (one of +,-,*,/): ")
        if  is_valid_operator(userInput):
            return userInput
        else:
            if not force_valid_input:
                return None
            print("Incorrect operator!")


def calc(operator, a, b): # calculates and returns the result of operation
    result = None
    match operator:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b
        case '/':
            if b == 0:
                print("Error: Division by zero")
                return None
            else:
                result = a / b
    return result


def simple_calculator(): # main function
    while True:
        firstNumber = ask_for_a_number(force_valid_input=False)
        if firstNumber == None:
            break
        
        operator = ask_for_an_operator(force_valid_input=True)
        secondNumber = ask_for_a_number(force_valid_input=True)
        result = calc(operator, firstNumber, secondNumber)
        
        if result is not None:
            print("The result equals ", result)
        
simple_calculator()










    

