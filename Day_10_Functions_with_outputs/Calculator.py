# Calculator
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


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculation():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for operator in operators:
        print(operator)

    switcher = True
    while switcher:

        operation_symbol = input("Pick an operator: ")
        calculation_function = operators[operation_symbol]
        num2 = float(input("What's the next number?: "))
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        wish = input("Do you want to continue? press y to continue n - to start again:")
        if wish == "y":
            num1 = answer
        else:
            switcher = False
            calculation()


calculation()
