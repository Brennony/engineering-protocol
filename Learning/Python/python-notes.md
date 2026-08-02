# Python Notes and Questions:

# What is Python?
Python is a high-level programming language designed with readability and simplicity in mind. Python uses syntax that is close to human language, making it easier to learn, write, and maintain compared to many lower-level languages.

Python is commonly used for:
- Web development
- Data science
- Artificial intelligence
- Automation
- Engineering applications
- Software development

---

# Why is Python popular?
Python is popular because of its:
- High readability
- Simple syntax
- Large community
- Massive library support
- Versatility across many industries

Python removes a lot of unnecessary complexity found in other languages. For example, variables do not require manually declaring their data types.

Python is beginner-friendly while still being powerful enough for professional applications.

---

# Variables:
Variables are containers that store information in memory.

Examples:

name = "Brennon"
age = 18
height = 6.0

Python variables can store:
- Strings
- Integers
- Floats
- Booleans
- Lists
- Other data structures

Python automatically determines the data type based on the value assigned.

---

# Data Types:

## Integer (int)
Whole numbers without decimals.

Examples:
```
5
100
-25
```

Used for:
- Counting
- Ages
- Quantities


## String (str)
A sequence of characters used to represent text.

Examples:
```
"Hello"
"Python"
"Brennon"
```

Strings can be manipulated using methods like:

.lower()
.upper()
.isalpha()


## Boolean (bool)
Represents True or False values.

Think of it like a light switch:

True = On
False = Off

Commonly used for:
- Conditions
- Decisions
- Logic


## Float (float)
Numbers containing decimals.

Examples:
```
3.14
5.5
-10.25
```

Used for:
- Scientific calculations
- Measurements
- Precise values

---

# Printing:
Printing displays information to the user.

Example:

print("Hello World")

You can also use f-strings to insert variables:

name = "Brennon"
print(f"Hello {name}")

Output:

Hello Brennon

---

# Input:
Input allows the user to provide information to the program.

Example:

name = input("What is your name? ")

The user enters a value, and Python stores it.

Almost every program follows this basic structure:

INPUT -----> ( OUR CODE ) -----> OUTPUT

Example:

User enters:
5

Python calculates:
5 + 5

Output:
10

---

# Comments:
Comments are notes written inside code that Python ignores.

Example:

# This prints the user's name
print(name)

Comments are used to:
- Explain code
- Organize programs
- Communicate with other programmers

---

# Basic Math:
Python has built-in mathematical operators.

Addition:
+

Subtraction:
-

Multiplication:
*

Division:
/

Modulus (remainder):
%

Exponent:
**

Example:

5 ** 2

Output:

25

---

# Functions:
Functions are reusable blocks of code designed to perform a specific task.

Creating a function:

def functionName():
    code

Calling a function:

functionName()

Functions help:
- Reduce repeated code
- Organize programs
- Make code easier to edit

---

# Parameters:
Parameters allow functions to receive information.

Example:

def greet(name):
    print(f"Hello {name}")

Calling:

greet("Brennon")

Output:

Hello Brennon

The value passed into the function becomes the parameter.

---

# Return Values:
Functions can send information back using return.

Example:

def add(x, y):
    return x + y

result = add(5, 10)

result now equals:

15

return does two things:
1. Sends information back
2. Ends the function

---

# Lists:
Lists store multiple values inside one variable.

Example:

numbers = [1, 2, 3, 4]

Lists are useful when storing many related values.

You can add values using:

numbers.append(5)

Result:

[1, 2, 3, 4, 5]

---

# For Loops:
For loops repeat code a specific number of times.

Example:

for i in range(5):
    print(i)

Output:

0
1
2
3
4

Important:
Python starts counting at 0.

range(5) creates:

0, 1, 2, 3, 4

not:

1, 2, 3, 4, 5

---

# The Loop Variable:
The variable after "for" stores the current value of the loop.

Example:

for i in range(3):
    print(i)

First loop:
i = 0

Second loop:
i = 1

Third loop:
i = 2

The variable name can be anything:

for banana in range(3):

works the same way.

---

# While Loops:
While loops repeat code while a condition is True.

Example:

while True:
    print("Running")

This creates an infinite loop unless stopped.

To stop a loop, use:

break

Example:

while True:
    answer = input("Continue? ")

    if answer == "no":
        break

---

# Combining For Loops and While Loops:
A common pattern is:

For loop:
Controls how many things you need.

While loop:
Makes sure each individual thing is valid.

Example:

for i in range(5):
    while True:
        get valid input
        break

This means:

"Get 5 valid inputs, but don't move on until each input works."

---

# Exception Handling:
Python can handle errors using try and except.

Example:

try:
    number = float(input("Enter number: "))

except ValueError:
    print("Invalid number")

If the user enters:

abc

Python normally crashes.

try/except catches the error and allows the program to continue.

---

# Input Validation:
Input validation makes sure users enter correct information.

Example:

while True:
    try:
        age = int(input("Age: "))
        break
    except ValueError:
        print("Enter a valid number")

The loop continues until the user provides valid input.

---

# Returning Multiple Values:
Functions can return multiple values.

Example:

def getNumbers():
    return 5, 10

num1, num2 = getNumbers()

Python actually returns a tuple:

(5, 10)

Then it unpacks the values into separate variables.

---

# Common Mistakes:

## Python is Case Sensitive:
These are different:

name

Name

NAME


## = vs ==:

=
Assigns a value.

Example:

x = 5


==
Checks if two values are equal.

Example:

if x == 5:


## Forgetting to Return:
A function without return gives back:

None


## Infinite Loops:
A while loop without a way to stop will run forever.

Example:

while True:
    print("Forever")


## Forgetting Indentation:
Python uses indentation to define blocks of code.

Incorrect:

if age > 18:
print("Adult")


Correct:

if age > 18:
    print("Adult")

---

# Programming Mindset:
Most programs follow this pattern:

INPUT
    |
    v
PROCESSING
    |
    v
OUTPUT

Good programmers focus on:
- Reducing repeated code
- Creating reusable functions
- Validating user input
- Making programs easy to modify later
