#None result
def add(x, y):

    print(x+y)

add(5, 8)
result = add(5,8)
print(result)

print()
print()
print()

#Some result in returning
def plus(x, y):
    return x + y
result = plus(5,8)
print(result)

#return word is terminating function

print()
print()
print()

#it is non recommended because of different types of data (num and string) but you can
def divide(divided, divisor):
    if divisor != 0:
        return divided/divisor
    else:
        return "fail"
result = divide(1, 2)
print(result)