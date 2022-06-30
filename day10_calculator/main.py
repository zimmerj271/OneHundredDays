import os
from art import logo
# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

def calculator():
    print(logo)
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    num1 = float(input("What's the first number?: "))
    for operator in operations:
        print(operator)

    calculating = True
    while calculating:

        operator = input("Pick an operation from the line above: ")    
        num2 = float(input("What's the second number?: "))
        calculation_function = operations[operator]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")

        if input(f"Would you like to continue calculating with {answer} [y/n]?: ") == 'y':
            num1 = answer
        else:
            calculating = False
            os.system('clear')
            calculator()

calculator()