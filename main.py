# This is a random password generator. The passwords that this program generates are a bit tricky and hard to remember. Once I learn AI I will make this more user friendly


import random
import string

alphabet_string = string.ascii_lowercase
# Create a string of all lowercase letters
# print(alphabet_string)

# alphabet_list = list(alphabet_string)

numbers = "123456789"


for i in range(3):
    AlphaPassPt = random.choice(alphabet_string)
    NumPassPt = random.choice(numbers)
    print(f"{AlphaPassPt}{NumPassPt}", end='')

# This program is a program that runs as a program like a program