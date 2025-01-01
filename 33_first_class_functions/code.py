from operator import itemgetter

def divide (dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can not be 0")
    return dividend/divisor

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find element {expected} expected")


def get_friend_name(friend):
    return(
        friend["name"]
    )


friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Ana", "age": 50},
    {"name": "Mari", "age": 33}
]

print(search(friends, "Ana", get_friend_name))



def calculate (*values, operator):
    return operator(*values)

result = calculate(20, 4, operator=divide)
#result1 = calculate(20, 4, 5, operator=divide)
print(result)
#print(result1)
print(divide)