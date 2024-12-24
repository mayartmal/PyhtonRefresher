numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]

print(doubled)



friends = ["ann", "bob", "serj", "art", "sonya"]
starts_s_control = []
starts_s = [x for x in friends if x.startswith("s")]

for friend in friends:
    if friend.startswith("s"):
        starts_s_control.append(friend)





print(starts_s_control)
print(starts_s)
