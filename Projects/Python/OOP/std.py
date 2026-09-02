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
        return f"Average Gpa: {avg}"

if __name__ == "__main__":
    student1 = Student("Brennon", 18, 3.5)
    student2 = Student("Eli", 19, 1.9)
    if student1.is_passing() == False:
        ans = input(f"Would you like to change {student1.name}'s GPA (y/n)?: ").strip().lower()
        if ans == "y":
            student1.update_gpa(4.0)
    if student2.is_passing() == False:
        ans = input(f"Would you like to change {student2.name}'s GPA (y/n)?: ").strip().lower()
        if ans == "y":
            student2.update_gpa(4.0)
    classroom = Classroom()
    classroom.add_student(student1)
    classroom.add_student(student2)
    classroom.display_all()
    print(classroom.class_average())

