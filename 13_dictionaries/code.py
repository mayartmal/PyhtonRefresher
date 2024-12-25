friend_ages  = {"Rolf": 24, "Anne": 26, "Diana": 33}
print(friend_ages["Rolf"])
friend_ages["Rolf"] = 20
print(friend_ages["Rolf"])
print()
friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Anne", "age": 50},
    {"name": "Kat", "age": 25}
]

print(friends[1]["name"])


print()


student_attendance = {"Rolf": 55, "Bob": 66, "Anne": 90}
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")


attendance_values = student_attendance.values()
print(sum(attendance_values) / len(student_attendance))





