total_bill = float(input("Welcome to the tip calculator.\nWhat was the total bill?$\n"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
people = int(input("How many people to split the bill?\n"))
tip_as_percent = tip / 100
x = total_bill * tip_as_percent / people
print(f"Each person should pay ${round(x, 2)}")
