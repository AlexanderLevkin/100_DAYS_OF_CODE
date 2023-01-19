# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# def greet():
#     print("Hello")
#     print("World")
#     print("!!!")
#
# greet()
# name - parameter
# def greet(name):
#     print(f"Hello {name}")
#     print(f"How are you, {name} ?")
#     print(f"isn't the nice weather today {name} ?")
# # Alexander - argument
#
# greet("Alexander")
#
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location} ?")
# greet_with("Alexander", "London")

#Write your code below this line 👇

# def paint_calc(paint_calc, width, cover ):
#     a = round(paint_calc/width*cover)
#     print(a)
#
#
#
# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.
#
# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(paint_calc=test_h, width=test_w, cover=coverage)

# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)