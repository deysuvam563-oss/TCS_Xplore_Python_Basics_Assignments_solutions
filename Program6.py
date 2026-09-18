class Student:
    def __init__(self, roll_no, name, marks, standard):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.standard = standard

    def calculate_percentage(self):
        return sum(self.marks) / 4

    def calculate_grade(self):
        percentage = self.calculate_percentage()

        if percentage >= 80:
            return 'A'
        elif percentage >= 60:
            return 'B'
        elif percentage >= 40:
            return 'C'
        else:
            return 'F'

    def promote(self):
        grade = self.calculate_grade()

        if grade != 'F':
            self.standard += 1
            return True
        return False

    def display(self):
        percentage = self.calculate_percentage()
        grade = self.calculate_grade()

        print("\nStudent Details")
        print("Roll Number:", self.roll_no)
        print("Name:", self.name)
        print("Standard:", self.standard)
        print("Percentage:", percentage)
        print("Grade:", grade)

        if self.promote():
            print("Result: Promoted to Standard", self.standard)
        else:
            print("Result: Not Promoted")

roll_no = int(input("Enter roll number: "))
name = input("Enter student name: ")
standard = int(input("Enter standard: "))

marks = []
for i in range(4):
    mark = float(input("Enter marks in subject " + str(i + 1) + ": "))
    marks.append(mark)

student = Student(roll_no, name, marks, standard)
student.display()
