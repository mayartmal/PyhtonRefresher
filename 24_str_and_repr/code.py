class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self):
    #     return f"{self.name} person with age of {self.age}"

    def __repr__(self):
        return f"<{self.name} person with age of {self.age}>"




bob = Person("Bob", 35)
print(bob)
print(f"{bob.name}")
