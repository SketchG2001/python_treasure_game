logo = '''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
print(logo)

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}
num1 = float(input("enter the value of num1. \n"))

for symbol in operations:
    print(symbol)
should_continue = True
while should_continue:
    operation_symbol = input("pick an operation: \n")
    num2 = float(input("what's the next number? \n"))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input(f"Type 'y' to continue calculating {answer}, or type 'n' to exit.: ").lower() == "y":
        num1 = answer
    else:
        should_continue = False
        print("Good Bye!")
    # operation_symbol = input("Pick another operation: ")
    # num3 = int(input("what's the next number? "))
    # calculation_function = operations[operation_symbol]
    # second_answer = calculation_function(calculation_function(num1,num2),num3)
    # print(f"{answer} {operation_symbol} {num3} = {second_answer}")
    # print( )