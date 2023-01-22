programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}

# Retrieving items from dictionary (пишем ключ но возврашает значание)
print(programming_dictionary["Function"])

# Adding new item to the dictionary
programming_dictionary["Loop"] = "This is new item"
print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}

# Wipe (потереть) an exiting dictionary
# programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"

# Loop through a dictionary
for thing in programming_dictionary:
    print(thing) 
    print(programming_dictionary[thing])
