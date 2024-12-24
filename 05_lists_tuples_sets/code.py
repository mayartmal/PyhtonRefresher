#list. can be modified. order is guarantied
l = ["Bob", "Rolf", "Anne"]

#tuple. cant be modified. order is guarantied
t = ("Bob", "Rolf", "Anne")

#set. all elements are uniq. order is not guarantied
s = {"Bob", "Rolf", "Anne"}

print(l[0])
print(t[0])

l[0] = "Smith"
print(l[0])

l.append("Bob")
print(l)

l.remove("Anne")
print(l)

s.add("Jane")
print(s)

s.add("Jane")
print(s)
