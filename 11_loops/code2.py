friends = ["Rolf", "Bob", "Anne", "Tim"]

for friend in friends:
    print(f"{friend} is my friend")


for friend in range(4):
    print(f"{friend} is my friend")


grades = [35, 55, 66, 77, 12, 56, 11]
total = 0
amount = len(grades)

for grade in grades:
    #total = total + grade
    total += grade
print(total/amount)


total = sum(grades)
print(total/amount)