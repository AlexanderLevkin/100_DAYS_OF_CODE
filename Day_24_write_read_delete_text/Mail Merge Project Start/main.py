# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    for name in names:
        search_text = "[name]"
        replace_text = name.replace("\n", "")
        with open(r'./Input/Letters/starting_letter.txt', 'r') as file2:
            data = file2.read()
            data = data.replace(search_text, replace_text)
        with open(f"./Output/ReadyToSend/Mail_for_{name}.txt", mode="w") as file2:
            file2.write(data)
