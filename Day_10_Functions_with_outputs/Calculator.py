# Calculator

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

num1 = int(input("What's the first number?: "))
for operator in operators:
    print(operator)
operation_symbol = input("Pick an operator from the line above: ")
calculation_function = operators[operation_symbol]
num2 = int(input("What's the second number?: "))
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = input("Pick another operation: ")
num3 = int(input("What's the second number?: "))
calculation_function = operators[operation_symbol]
second_answer = calculation_function(calculation_function(num1, num2), num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")