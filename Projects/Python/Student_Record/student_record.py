# Brennon York  |  Student Record v2.0 |  8/6/2026

# Version 2.1: I added file-creating functionality. It will be improved more soon!
#   Tomorrow... I add file opening and maybe deleting capabilities if possible.

import csv
import os
import statistics

record = []

def main():
    print("--------------------------")
    print("--Student Record Program--")
    print("--------------------------\n")
    while True:
        choice = getFunction()
        if choice == 0:
            break
        elif choice == 1:
            listStudent()
        elif choice == 2:
            displayStudent()
        elif choice == 3:
            addStudent()
        elif choice == 4:
            deleteStudent()
        else:
            break
        # Again?
        again = input("Would you like to quit (y/n)?: ")
        if again == "y":
            break
        else:
            print("")

def getFunction():
    print("-Please select a function-")
    print("1. List Students and Number")
    print("2. Display Student Information")
    print("3. Add Students")
    print("4. Delete Students")
    print("0. Quit Program")
    print("(Select function number listed)")
    print("--------------------------\n")
    while True:
        Function = input("")
        try:
            if 0 <= int(Function) <= 4:
                break
            else:
                print("Please enter a valid number (1-4)")
        except ValueError:
            print("Please enter a valid number (1-4)")
    return int(Function)

def listStudent():
    if not record:
        print("There are no students in directory!\n")
    else:
        print ("--Students in Directory--\n")
        for i, student in enumerate(record, start=1):
            print(f"{i}. {student['Name']}")

def addStudent():
    name = getName()
    age = getAge()
    major = getMajor()
    gpa = getGpa()
    data = {"Name": name, "Age": age, "Major": major, "Gpa": gpa,}
    record.append(data)
    with open("student_record.csv", "a", newline="") as file:
        fieldnames = ["Name", "Age", "Major", "Gpa"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(data)

def deleteStudent():
    listStudent()
    while True:
        if not record:
            break
        try:
            choice = int(input("\nWhich student would you like to delete?: "))
            if 1 <= choice <= len(record):
                del record[choice - 1]
                print("Student deleted successfully.")
                break
            else:
                print("That student number doesn't exist.")
        except ValueError:
            print("Please enter a valid student number.")

def getName():
    student = str(input("Student Name: "))
    return student.title().strip()

def getAge():
    while True:
        Age = input("Age: ")
        try:
            return int(Age)
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
    if not record:
        print("There are no students in directory!\n")
    else:
        for i, student in enumerate(record, start=1):            
            print()
            print(f"--Student {i+1}--")
            print(f"Name: {student["Name"]}")
            print(f"Age: {student["Age"]}")
            print(f"Major: {student["Major"]}")
            print(f"Gpa: {student["Gpa"]}")

def getFile():
    quit            

# Actual Program
main()