# Calculator functions

from art import logo
print(logo)


def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

# create a dictionary where keys are symbols and values are their functions

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

# num1 = int(input("What's the FirstNumber? : "))

# for symbol in operations:
#     print(symbol)

# operation_symbol = input("Pick an operation from the line above: ")

# num2 = int(input("What's the SecondNumber? : "))
    

# calculation_function = operations[operation_symbol]

# first_answer = calculation_function(num1,num2)


# print(f"{num1} {operation_symbol} {num2} = {first_answer}")

# -----------------------------------------

# operation_symbol = input("Pick another operation: ")

# num3 = int(input("What's the next number?: "))

# calculation_function = operations(operation_symbol)

# second_answer = calculation_function(calculation_function(num1,num2), num3)

# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}") 


def calculator():
    num1 = float(input("What's the FirstNumber? : "))

    for symbol in operations:
        print(symbol)



    is_stop = False

    while not is_stop:

        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the Next Number? : "))
            

        calculation_function = operations[operation_symbol]

        answer = calculation_function(num1,num2)


        print(f"{num1} {operation_symbol} {num2} = {answer}")

    


        calucating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit. Or if you continue with new values type 'new': ")

        if calucating == "n":
            is_stop = True
            print("Good bye")
        
        elif calucating == "y":
            num1 = answer

        elif calucating =='new':
            calculator()
    

calculator()