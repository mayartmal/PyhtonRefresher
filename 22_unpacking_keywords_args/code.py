def named(**kwargs):
    print(kwargs)

named(name="Bob", age=25)

def named2(name, age):
    print(name, age)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

def both(*args, **kwargs):
    print(args)
    print(kwargs)



details = {"name": "Bob", "age": 25}
named2(**details)

print_nicely(name="Bob", age=25)

both(1, 3, 5, name="bob", age=26)