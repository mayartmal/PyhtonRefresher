x = (5, 11)
y = 5, 11
print(x)
print(y)
x1, x2 = 5, 11
y1, y2 = y
print(x1)
print(x2)
print(y1)
print(y2)



print()
print()
print()

student_attendance = {"Rolf": 55, "Bob": 66, "Anne": 90}
print(list(student_attendance.items()))
for s, a in student_attendance.items():
    print(s)
    print(a)
    #print(f"{student}: {attendance}")



people = [
    ("Bob", 42, "Mechanic"),
    ("James", 33, "Engineer"),
    ("Alex", 55, "Artist")
]

for name, age, profession in people:
    print(f"Name {name}, Age {age}, Profession {profession}")

print()

for person in people:
    print(f"Name {person[0]}, Age {person[1]}, Profession {person[2]}")

print()

for name, _, profession in people:
    print(f"Name {name}, Profession {profession}")


print()
head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)
