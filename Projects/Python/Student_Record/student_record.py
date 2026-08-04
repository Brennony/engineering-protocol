# Brennon York  |  Student Record v1.0 |  8/3/2026

# First Version works somewhat well. Could use some more tweaking and feature!

import statistics

record = []


def main():
    name = getName()
    age = getAge()
    major = getMajor()
    gpa = getGpa()
    data = {"Name": name, "Age": age, "Major": major, "Gpa": gpa,}
    record.append(data)

def getName():
    student = str(input("Student Name: "))
    return student.title().strip()

def getAge():
    while True:
        Age = input("Age: ")
        try:
            int(Age)
            return Age
        except ValueError:
            print("Please enter a valid age and try again (Whole number): ")

def getMajor():
    major = str(input("Major: "))
    return major.title().strip()

def getGpa():
    while True:
        try:
            Gpa = float(input("GPA: "))
            if 0.0 <= Gpa <= 4.0:
                return Gpa
            else:
                print("Please enter a valid GPA and try again: ")
        except ValueError:
            print("Please enter a valid GPA and try again: ") 

def displayStudent():
    for i in range(len(record)):
        print()
        print(f"--Student {i+1}--")
        print(f"Name: {record[i]['Name']}")
        print(f"Age: {record[i]['Age']}")
        print(f"Major: {record[i]['Major']}")
        print(f"Gpa: {record[i]['Gpa']}")


while True:
    main()
    displayStudent()

    again = input("Would you like to go again (enter 'y' if yes)?: ")
    if again.lower().strip() != 'y':
        break