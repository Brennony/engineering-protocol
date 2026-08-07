# Brennon York  |  About Me v1.1  |  7/30/2026

# Changed Names of Functions and Replaced Repeated Code

# My Functions
def ageClass(age):
    if age >= 18:
        print("You are an adult!")
    else:
        print("You are a minor!")
def techMajor(major):
    major = major.lower()
    if "computer" or "sofware" or "engineer" in major:
        print("Hey, me too!")
def pythonLang(favlang):
    if favlang.lower() == "python":
        print(f"{favlang}, You know ball!")
    else:
        print(favlang)
def validName(name):
    name = input("What is your name? ")
    while True:
        if name.isalpha():
            return name
        print("Please enter a valid name (letters only).")
        name = input("What is your name? ")

# Main Program
while True:
    # Get our Variables
    name = ''
    validName(name)
    age = int(input("How old are you (ONLY answer with numbers)? "))
    major = input("What is your major? ")
    job = input("If you could have any job in the world, what would it be? ")
    favlang = input("What is your favorite programming language (you know it's python)? ")

    # Print out the results
    print(f"Hello {name}!, you are {age} years old.")
    ageClass(age)
    print()
    print("Major:")
    print(major)
    techMajor(major)
    print()
    print("Dream Career:")
    print(job)
    print()
    print("Favorite Programming Language:")
    pythonLang(favlang)
    print()
    print("Thanks for using my python program! I hope you enjoyed! ")

    # Rerun?
    again = input("Rerun (y/n)?: ").lower()
    while True:
        if again not in ('y', 'n'):
            again = input("Enter Valid Answer (y/n): ").lower()
        else:
            break
    if again == 'n':
        break