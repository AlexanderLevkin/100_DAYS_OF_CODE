# 🚨 Don't change the code below 👇
age = input("What is your current age?\n ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
days_age = int(age)*365
week_age = int(age)*52
month_age = int(age)*12

days_remain = 90 * 365 - days_age
week_remain = 90 * 52 - week_age
month_remain = 90 * 12 - month_age
print(f"You have {days_remain} days, {week_remain} weeks, and {month_remain} months left.")

