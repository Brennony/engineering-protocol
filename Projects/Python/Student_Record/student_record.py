# Brennon York  |  Student Record v2.4 |  9/10/2026

# Versions 2.4: Added loading student_record and more capabilities

import json
import csv
import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "student_record.json")


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


class Student:
    count = 0

    # Initialization of Class Student
    def __init__(self,name,age,major,gpa,bio="",
                 work_experience=None,volunteer_work=None,
                 skills=None,current_employment=""):
        self.name = name
        self.age = age
        self.major = major
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


    # Additional Functions
    def __str__(self):
        return f"Name: {self.name} | Age: {self.age} | GPA: {self.gpa}"

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
            "gpa": self.gpa,
            "bio": self.bio,
            "work_experience": [f"{e.title}, {e.company}, {e.start}, {e.end}" 
                for e in self.work_experience],
            "volunteer_work": [f"{v.title}, {v.organization}, {v.hours}"
                for v in self.volunteer_work],
            "skills": [s.skill for s in self.skills],
        }


class GradStudent(Student):
    def __init__(self, name, age, gpa, major, thesis_topic):
        super().__init__(name,age,major,gpa)
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

def askPassing(stud):
    if stud.is_passing() == False:
        ans = input(f"Would you like to change {stud.name}'s GPA (y/n)?: ").strip().lower()
        if ans == "y":
            stud.update_gpa(4.0)



# Main

record = []

def main():
    loadStudents()
    student = addStudent()
    record.append(student)
    saveStudents()
    for stu in record:
        print(stu)


def addStudent():
    # Easy Inputs
    name = input("Enter student's name: ")
    age = int(input(f"How old is {name}?: "))
    major = input(f"What is {name}'s major?: ")
    gpa = float(input(f"What is {name}'s GPA?: "))
    bio = input(
        f"Enter a biography for {name} that is between 100-750 characters"
        "or enter nothing:\n"
        )
    
    # Work Experience Input
    while True:
        work_experience = input(
            "==Work Experience Format==\n"
            "'Job Title, Company, MonthYr, Present'\n"
            "(e.g. 'Software Engineer, Google, Jan2024, Mar2025').\n"
            f"Please enter work experience for {name} (or press Enter to skip):\n"
        ).strip()
        if work_experience == "":
            work_experience = None
            break
        try:
            Employment.from_string(work_experience)
            break
        except ValueError as e:
            print(f"Error: {e}\nPlease try again.\n")

    # Volunteer Work Input
    while True:
        volunteer_work = input(
            "==Volunteer Work Format==\n"
            "'Volunteer Title, Organization/Company, Hours Worked'\n"
            "(e.g. 'Chef, NY Homeless Shelter, 225')\n"
            f"Please enter volunteer experience for {name} as shown above:\n"
        ).strip()
        if volunteer_work == "":
            volunteer_work = None
            break
        try:
            Volunteering.from_string(volunteer_work)
            break
        except ValueError as e:
            print(f"Error: {e}\nPlease try again.\n")

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
    student = Student(name,age,major,gpa,bio,work_experience,volunteer_work,skills)
    return student


def saveStudents():
    with open(JSON_PATH, "w") as file:
        json.dump([s.to_dict() for s in record], file, indent=2)

def loadStudents():
    try:
        with open(JSON_PATH, "r") as file:
            data = json.load(file)
            for d in data:
                student = Student(
                    d["name"], d["age"], d["major"], d["gpa"],
                    d["bio"], d["work_experience"], 
                    d["volunteer_work"], d["skills"]
                )
                record.append(student)
    except FileNotFoundError:
        return


if __name__ == "__main__":
    main()




# Old Code:
"""
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

def getFunction():
    print("--------------------------")
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
    saveStudents()

def deleteStudent():
    listStudent()
    while True:
        if not record:
            break
        try:
            choice = int(input("\nWhich student would you like to delete?: "))
            if 1 <= choice <= len(record):
                del record[choice - 1]
                saveStudents()
                print("Student deleted successfully.")
                break
            else:
                print("That student number doesn't exist.")
        except ValueError:
            print("Please enter a valid student number.")

def getName():
    while True:
        student = str(input("Student Name: "))
        if student.isalpha():
            return student.title().strip()
        else:
            print("Please enter only letters.\n")

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
            print(f"--Student {i}--")
            print(f"Name: {student["Name"]}")
            print(f"Age: {student["Age"]}")
            print(f"Major: {student["Major"]}")
            print(f"Gpa: {student["Gpa"]}\n")
         
def loadStudents():
    try:
        with open("student_record.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["Age"] = int(row["Age"])
                row["Gpa"] = float(row["Gpa"])
                record.append(row)
    except FileNotFoundError:
        return

def saveStudents():
    with open("student_record.csv", "w", newline="") as file:
        fieldnames = ["Name", "Age", "Major", "Gpa"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()
            for student in record:
                writer.writerow(student)


"""