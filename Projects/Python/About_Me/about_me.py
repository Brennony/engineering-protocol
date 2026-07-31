# Brennon York  |  Beta 1.0 Prototype of about_me.py  |  7/30/2026

# My Functions
def agefunc(age):
    if age >= 18:
        print("You are an adult!")
    else:
        print("You are a minor!")
def majorfunc(major):
    if "computer" in major.lower() or "engineer" in major.lower():
        print("Hey, me too!")
def langfunc(favlang):
    if favlang.lower() == "python":
        print(f"{favlang}, You know ball!")
    else:
        print(favlang)
def validname(name):
    while True:
        if name.isalpha():
            return name
        print("Please enter a valid name (letters only).")
        name = input("What is your name? ")

# Get our Variables
name = input("What is your name? ")
name = validname(name)
age = int(input("How old are you (ONLY answer with numbers)? "))
major = input("What is your major? ")
job = input("If you could have any job in the world, what would it be? ")
favlang = input("What is your favorite programming language (you know it's python)? ")

# Print out the results
print(f"Hello {name}!, you are {age} years old.")
agefunc(age)
print("")
print("Major:")
print(major)
majorfunc(major)
print("")
print("Dream Career:")
print(job)
print("")
print("Favorite Programming Language:")
langfunc(favlang)
print("")
print("Thanks for using my python program! I hope you enjoyed! ")

# Rerun?
# WILL FINISH LATER