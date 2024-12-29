def add(x, y):
    result = x + y
    print(result)

def say_hello(name, surname):
    print(f"Hello {name} {surname}")

def divide(divided, divisor):
    if divisor != 0:
        print(divided/divisor)
    else:
        print("fail")



add(5,3)
say_hello("bob", "tax")
say_hello(surname="tax", name="bob")
divide(9,3)
divide(9, 0)

