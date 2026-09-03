class Student:
    def __init__(self,name,age,gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def __str__(self):
        return f"Name: {self.name} | Age: {self.age} | GPA: {self.gpa}"

    def is_passing(self):
        return self.gpa >= 2.0

    def update_gpa(self,new_gpa):
        self.gpa = new_gpa
        print("GPA Changed")

class GradStudent(Student):
    def __init__(self, name, age, gpa, thesis_topic):
        super().__init__(name,age,gpa)
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


if __name__ == "__main__":
    student1 = Student("Brennon", 18, 3.5)
    student2 = Student("Eli", 19, 1.9)
    student3 = GradStudent("Jacob", 22, 3.7, "Eucharistic Miracles")
    askPassing(student1), 
    askPassing(student2), 
    askPassing(student3)
    classroom = Classroom()
    classroom.add_student(student1), classroom.add_student(student2), classroom.add_student(student3)
    classroom.display_all()
    student3.defend
    print(classroom.class_average())

