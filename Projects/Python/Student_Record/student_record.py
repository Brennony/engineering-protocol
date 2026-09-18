# Brennon York  |  Student Record v2.5 |  9/11/2026

# Versions 2.5: Started pushing old student_record capabilities to new program

import json
import re
import os
import textwrap


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "student_record.json")


# ==================== Record Entry Classes ====================
# These classes represent individual entries (work, volunteering, skills)
# that get attached to a Student. Each has a from_string() parser that
# validates and builds an instance from a formatted input string.

class Employment:
    _PATTERN = re.compile(
        r'^(?P<title>[A-Za-z0-9&.\'\- ]+),\s*'
        r'(?P<company>[A-Za-z0-9&.\'\- ]+),\s*'
        r'(?P<start>(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\d{4}),\s*'
        r'(?P<end>(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\d{4})$'
    )
    _PATTERN2 = re.compile(
        r'^(?P<title>[A-Za-z0-9&.\'\- ]+),\s*'
        r'(?P<company>[A-Za-z0-9&.\'\- ]+),\s*'
        r'(?P<start>(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\d{4}),\s*'
        r'(?P<end>Present)$'
    )

    def __init__(self, title, company, start, end):
        self.title = title
        self.company = company
        self.start = start
        self.end = end

    @classmethod
    def from_string(cls, text):
        match = cls._PATTERN.match(text) or cls._PATTERN2.match(text)
        if not match:
            raise ValueError(
                f"Invalid Work Experience Format: {text!r}. "
                "Expected: 'Job Title, Company, MonthYr, MonthYr' or "
                "'Job Title, Company, MonthYr, Present'... "
                "(e.g. 'Software Engineer, Google, Jan2024, Mar2025')."
            )
        return cls(**match.groupdict())

    def __str__(self):
        return f"{self.title} at {self.company} ({self.start} - {self.end})"


class Volunteering:
    _PATTERN = re.compile(
        r'^(?P<title>[A-Za-z0-9&.\'\- ]+),\s*'
        r'(?P<organization>[A-Za-z0-9&.\'\- ]+),\s*'
        r'(?P<hours>\d{1,4})$'
    )

    def __init__(self, title, organization, hours):
        self.title = title
        self.organization = organization
        self.hours = hours

    @classmethod
    def from_string(cls, text):
        match = cls._PATTERN.match(text)
        if not match:
            raise ValueError(
                f"Invalid Volunteer Work Format: {text!r}. "
                "Expected: 'Volunteer Title, Organization/Company, Hours Worked'... "
                "(e.g. 'Chef, NY Homeless Shelter, 225')"
            )
        return cls(**match.groupdict())

    def __str__(self):
        return f"{self.title} at {self.organization} (Hours: {self.hours})"


class Skills:
    _PATTERN = re.compile(r'^(?:\w+\s?){1,5}$')

    def __init__(self, skill):
        self.skill = skill

    @classmethod
    def from_string(cls, text):
        if not cls._PATTERN.match(text):
            raise ValueError(
                f"Invalid Skill format: {text!r}. "
                "Skills must be 1 to 5 words long for them to be recorded."
            )
        return cls(text.strip())

    def __str__(self):
        return self.skill


# ==================== Core Student Classes ====================
# Student is the main record type. GradStudent extends it with a thesis
# topic, and Classroom holds a group of Students together.

class Student:
    count = 0

    # Initialization of Class Student
    def __init__(self,name,age,major,minor,gpa,bio="",
                 work_experience=None,volunteer_work=None,
                 skills=None,current_employment=""):
        self.name = name
        self.age = age
        self.major = major
        self.minor = minor
        self.gpa = gpa
        self.bio = bio
        self.work_experience = work_experience
        self.volunteer_work = volunteer_work
        self.skills = skills
        self.current_employment = current_employment
        Student.count += 1


    # ----Properties of Class Student----
    # Properties of Name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 50:
            self.__name = value 
        else:
            raise ValueError("Name length must be between 0-50 chars.")

    # Properties of Age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 5 <= value <= 120:
            self.__age = value
        else:
            raise ValueError("Age must be between 5-120.")

    # Properties of Major
    @property
    def major(self):
        return self.__major

    @major.setter
    def major(self, value):
        if not re.search(r'[\t\n]', value) and len(value) < 51:
            self.__major = value
        else:
            raise ValueError("Major must be less than 51 chars and contain no tabs/newlines.")

    # Properties of Minor
    @property
    def minor(self):
        return self.__minor

    @minor.setter
    def minor(self, value):
        if value is None or value == "":
            self.__minor = ""
            return
        else:
            if not re.search(r'[\t\n]', value) and len(value) < 51:
                self.__minor = value
            else:
                raise ValueError("Minor must be less than 51 chars and contain no tabs/newlines.")

    # Properties of GPA
    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        if 0.0 <= float(value) <= 4.0:
            self.__gpa = value
        else:
            raise ValueError("GPA must be between 0.0 and 4.0")

    # Properties of Biography
    @property
    def bio(self):
        return self.__bio

    @bio.setter
    def bio(self, value):
        if len(value) == 0 or 100 <= len(value) <= 750:
            self.__bio = value
        else:
            raise ValueError("Bio must be empty, or between 100 and 750 chars.")

    # Properties of Work Experience
    @property
    def work_experience(self):
        return self.__work_experience

    @work_experience.setter
    def work_experience(self, value):
        if value is None:
            self.__work_experience = []
            return
        raw_entries = value if isinstance(value, list) else [value]
        self.__work_experience = [Employment.from_string(i) for i in raw_entries]

    # Properties of Volunteer Work
    @property
    def volunteer_work(self):
        return self.__volunteer_work

    @volunteer_work.setter
    def volunteer_work(self, value):
        if value is None:
            self.__volunteer_work = []
            return
        raw_entries = value if isinstance(value, list) else [value]
        self.__volunteer_work = [Volunteering.from_string(i) for i in raw_entries]

    # Properties of Skills
    @property
    def skills(self):
        return self.__skills

    @skills.setter
    def skills(self, value):
        if value is None:
            self.__skills = []
            return
        raw_entries = value if isinstance(value, list) else [value]
        self.__skills = [Skills.from_string(i) for i in raw_entries]


    # Printing Functions
    def __str__(self):
        return (
            f"Name: {self.name} | Age: {self.age} | "
            f"Major: {self.major} | GPA: {self.gpa} | "
            f"Jobs: {len(self.work_experience)} | "
            f"Volunteer: {len(self.volunteer_work)} | "
            f"Skills: {len(self.skills)}"
        )

    def display(self):
        width = max(45, len(self.name) + 10)

        print("╔" + "═" * width + "╗")
        print("║ " + self.name.center(width - 2) + " ║")
        print("╚" + "═" * width + "╝")

        status = "Passing" if self.is_passing() else "Not passing"
        print(f"  Age: {self.age:<10} Major: {self.major}")
        if self.minor:
            print(f"                  Minor: {self.minor}")
        print(f"  GPA: {self.gpa:<10.2f} Status: {status}")

        print("\n  ── Student Bio " + "─" * (width - 16))
        if self.bio:
            for line in textwrap.wrap(self.bio, width=width-4):
                print(f"    {line}")
        else:
            print("    No biography provided.")

        print("\n  ── Work Experience " + "─" * (width - 20))
        if self.work_experience:
            for job in self.work_experience:
                print(f"    • {job}")
        else:
            print("    None listed")

        print("\n  ── Volunteer Work " + "─" * (width - 19))
        if self.volunteer_work:
            for work in self.volunteer_work:
                print(f"    • {work}")
        else:
            print("    None listed")

        print("\n  ── Skills " + "─" * (width - 11))
        if self.skills:
            print("    " + ", ".join(str(s) for s in self.skills))
        else:
            print("    None listed")

        print()


    # Additional Functions
    def is_passing(self):
        return self.gpa >= 2.0

    def update_gpa(self,new_gpa):
        self.gpa = new_gpa
        print("GPA Changed")

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "major": self.major,
            "minor": self.minor,
            "gpa": self.gpa,
            "bio": self.bio,
            "work_experience": [f"{e.title}, {e.company}, {e.start}, {e.end}" 
                for e in self.work_experience],
            "volunteer_work": [f"{v.title}, {v.organization}, {v.hours}"
                for v in self.volunteer_work],
            "skills": [s.skill for s in self.skills],
        }


class GradStudent(Student):
    def __init__(self, name,age,major,minor,gpa,bio,
                 work_experience,volunteer_work,
                 skills,current_employment,thesis_topic):
        super().__init__(name,age,major,minor,gpa,bio,
                         work_experience,volunteer_work,
                         skills,current_employment)
        self.thesis_topic = thesis_topic

    def defend(self):
        print(f"{self.name} is defending their thesis on {self.thesis_topic}")

    def __str__(self):
        return f"{super().__str__()} | Thesis: {self.thesis_topic}"


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all(self):
        print("=====Classroom=1=====")
        print(f"Amount of students in class: {Student.count}")
        for student in self.students:
            print(student)

    def class_average(self):
        if len(self.students) == 0:
            return "No students enrolled in class."
        total = sum(student.gpa for student in self.students)
        avg = total / len(self.students)
        return f"Average Gpa: {avg:0.2f}"


# ==================== Global State ====================

record = []


# ==================== Menu / Interface Functions ====================
# Handles printing the menu, reading the user's menu choice, and routing
# that choice to the correct action.

def printInterface(input):
    width = max(45, len(input) + 10)
    print("╔" + "═" * width + "╗")
    print("║ " + input.center(width - 2) + " ║")
    print("╚" + "═" * width + "╝")

def printMenu():
    printInterface("Student Record Program")
    print("     0. Quit Program")      
    print("     1. Student List")
    print("     2. Display Student Info")
    print("     3. Add Students")
    print("     4. Delete Students")
    print("     5. GPA Checker")
    print("     6. Clear Records\n\n")

def menuInput():
    while True:
        try:
            f = int(input("Please choose a function to perform: "))
            if f in (0,1,2,3,4,5,6):
                break 
        except ValueError:
            print("      ── Invalid Input ── ")
        else: 
            print("      ── Invalid Input ── ")
    return f

def displayInput():
    print("1. Display all")
    print("2. Display a student")
    n = input("Please choose a function to perform: ").strip().lower()
    if n == "1":
        return 1
    elif n == "2":
        return 2
    else:
        return None

def sortInput(f):
    match f:
        case 1:
            listStudent()
        case 2:
            s = displayInput()
            if s == 1:
                for stu in record:
                    stu.display()
            elif s == 2:
                listStudent()
                if record:
                    displayStu(s)
        case 3:
            student = addStudent()
            record.append(student)
            saveStudents()
        case 4:
            deleteStudent()
        case 5:
            listStudent()
            askPassing()
        case 6:
            clearRecord() 


# ==================== Student Management Functions ====================
# Functions that operate directly on the `record` list: listing,
# adding, deleting, clearing, and displaying individual students.

def listStudent():
    if not record:
        print("There are no students in directory!\n")
    else:
        printInterface("Students in Directory")
        for i, student in enumerate(record, start=1):
            print(f"    {i}. {student.name}, {student.major}")

def addStudent():
    # Easy Inputs
    name = input("Enter student's name: ")
    age = int(input(f"How old is {name}?: "))
    major = input(f"What is {name}'s major?: ")
    minor = input(f"{name}'s Minor? (or press Enter to skip): ")
    gpa = float(input(f"What is {name}'s GPA?: "))
    bio = input(
        f"Enter a biography for {name} that is between 100-750 characters "
        "or enter nothing:\n"
        )

    # Work Experience Input
    work_experiences = []
    while True:
        try:
            k = int(input("How many work experiences to add? (0 to skip): "))
            if 0 <= k <= 10:
                break
        except ValueError:
            print("Please enter a valid number.")

    print(f"Work Experience Format:"
            "'Job Title, Company, MonthYr, Present'... "
            "(e.g. 'Software Engineer, Google, Jan2024, Mar2025').\n")
    
    for _ in range(k):
        while True:
            entry = input("Enter work experience: ").strip()
            try:
                Employment.from_string(entry)
                work_experiences.append(entry)
                break
            except ValueError as e:
                print(f"Error: {e}\nPlease try again.\n")

    work_experience = work_experiences if work_experiences else None

    volunteer_experiences = []
    while True:
        try:
            k = int(input("How many volunteer experiences to add (0 to skip): "))
            if 0 <= k <= 10:
                break
        except ValueError:
            print("Please enter a valid number.")

    print(f"Volunteer Work Format:"
            "'Volunteer Title, Organization/Company, Hours Worked'"
            "(e.g. 'Chef, NY Homeless Shelter, 225')\n"
          )

    for _ in range(k):
        while True:
            entry = input("Enter volunteer experience: ").strip()
            try:
                Volunteering.from_string(entry)
                volunteer_experiences.append(entry)
                break
            except ValueError as e:
                print(f"Error: {e}\nPlease try again.\n")

    volunteer_work = volunteer_experiences if volunteer_experiences else None

    # Skills Input
    skills = []
    while True:
        try:
            k = int(input("Enter number of skills to input (1-10): "))
            if 0 < k < 11:
                break
        except ValueError:
            print("Please enter a valid number.")
        else:
            continue

    for _ in range(k):
        skill = input(f"Please enter a skill that {name} has: ")
        skills.append(skill)

    # Return
    student = Student(name,age,major,minor,gpa,bio,work_experience,volunteer_work,skills)
    return student

def deleteStudent():
    listStudent()
    while True:
        if not record:
            break
        try:
            choice = int(input("\n      Which student would you like to delete?: "))
            if 1 <= choice <= len(record):
                del record[choice - 1]
                saveStudents()
                print("Student deleted successfully.")
                break
            elif 0 == choice:
                break
            else:
                print("That student number doesn't exist.")
        except ValueError:
            print("Please enter a valid student number or quit (enter 0).")

def clearRecord():
    n = input("Are you sure you want to clear record (y/n)?: ").strip().lower()
    if n == "y":
        record.clear()
        saveStudents()

def displayStu(s):
    try:
        n = int(input("Choose a student: "))
        if 1 <= n <= len(record):
            record[n - 1].display()
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def askPassing():
    try:
        n = int(input("Choose a student: "))
        if 1 <= n <= len(record):
            student = record[n - 1]
            if not student.is_passing():
                ans = input(f"Would you like to change {student.name}'s GPA (y/n)?: ").strip().lower()
                if ans == "y":
                    gpa = float(input("New GPA: "))
                    student.update_gpa(gpa)
                    saveStudents()
            else:
                print(f"{student.name}'s GPA is {student.gpa:.2f} — Passing.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")


# ==================== Persistence Functions (Save/Load) ====================
# Reads and writes the `record` list to student_record.json.

def saveStudents():
    with open(JSON_PATH, "w") as file:
        json.dump([s.to_dict() for s in record], file, indent=2)

def loadStudents():
    try:
        with open(JSON_PATH, "r") as file:
            data = json.load(file)
            for d in data:
                student = Student(
                    d["name"], d["age"], d["major"], d.get("minor", ""), 
                    d["gpa"], d["bio"], d["work_experience"], 
                    d["volunteer_work"], d["skills"]
                )
                record.append(student)
    except FileNotFoundError:
        return


# ==================== Program Entry Point ====================

def main():
    loadStudents()
    while True:
        printMenu()
        f = menuInput()
        if f == 0:
            break
        else:
            sortInput(f)


if __name__ == "__main__":
    main()