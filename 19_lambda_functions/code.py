#lambda functions is used for input values and output values. not for actions!
def add(x, y):
    return x+ y
print(add(1,1))


print((lambda x, y: x + y)(5, 7))


def double(x):
    return x * 2
sequence  = [1, 3, 5, 9]

#similar
doubled = [double(x) for x in sequence]
print(doubled)
doubled2 = map(double, sequence)
print(doubled2)


#using lambda
print()
print()
doubled3 = [(lambda x: x*2)(x) for x in sequence]
#add list when using a map function
doubled4 = list(map(lambda x: x*2, sequence))
print(doubled3)
print(doubled4)
