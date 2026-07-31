# Brennon York  |  Alpha Prototype of about_me.py  |  7/30/2026

# Imported functions
from gettext import find

# Get our Variables
name = input("What is your name? ")
age = int(input("How old are you? "))
major = input("What is your major? ")
job = input("If you could have any job in the world, what would it be? ")
favlang = input("What is your favorite programming language (you know it's python)? ")

# Weed out invalid inputs
while True:
    if name.isalpha():
        break
    else:
        print("Please enter a valid name (letters only).")
        name = input("What is your name? ")

# Print out the results
print(f"Hello {name}!, you are {age} years old.")
if age >= 18:
    print("You are an adult!")
else:
    print("You are a minor!")
print("")
print("Major:")
print(major)
if major.lower().find("computer") != -1 or major.lower().find("engineer") != -1:
    print("Hey, me too!")
print("")
print("Dream Career:")
print(job)
print("")
print("Favorite Programming Language:")
if favlang.lower() == "python":
    print(f"{favlang}, You know ball!")
else:
    print(favlang)
print("")
print("Thanks for using my python program! I hope you enjoyed!")