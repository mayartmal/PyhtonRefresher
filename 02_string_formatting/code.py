name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)
with_name_2 = greeting.format("Rolf")

print(with_name)
print(with_name_2)

with_name_3 = f"Hello, {name}"
print(with_name_3)