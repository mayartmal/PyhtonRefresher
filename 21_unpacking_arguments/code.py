def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total

def add(x, y):
    return x + y

def plus(*args):
    return sum(args)

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    if operator == "+":
        return sum(args)
    else:
        return "Unexpected operator"


multiply(1, 3, 'a')
print(multiply(1, 3, 'a'))


nums = [3, 5]
print(add(*nums))

nums2 = {"x": 1, "y": 3}
print(add(nums2["x"], nums2["y"]))
print(add(x = nums2["x"], y = nums2["y"]))
print(add(**nums2))

print(apply(1, 3, 2, operator="+"))
print(apply(1, 3, 2, operator="*"))