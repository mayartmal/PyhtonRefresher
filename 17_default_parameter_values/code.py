def add(x, y = 1):
    print(x + y)

add(5)
add(1, 1)
add(x=5, y=5)
add(y=3, x=1)


print()
print()
print()


#example of a bad practice
default_y = 3
def plus(x, y = default_y):
    sum = x + y
    print(sum)
plus(2)
default_y = 10
plus(2)
