sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

sentence_list = sentence.split()
result = {name: len(name) for name in sentence_list}
# Write your code below:

print(result)
