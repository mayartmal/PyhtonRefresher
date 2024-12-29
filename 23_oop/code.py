class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades)/len(self.grades)

student = Student("Bob", (89, 90, 56, 70, 98))
student2= Student("Rolf", (100, 90, 100, 71, 56))
print(student.name)
print(student.grades)
print(Student.average(student))
print((student.average()))
print((student2.average()))
#print(student.average())

#student = {"name": "Rolf", "grades": (89, 90, 56, 70, 98)}

#def average(sequence):
#    return sum(sequence)/len(sequence)
#print(average(student["grades"]))
