class ClassTest:
    #for data inside object
    def instance_method(self):
        print(f"Called instance method of {self}")


    #for factories
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    #code organisation or something like that
    @staticmethod
    def static_method():
        print("Static method")


test = ClassTest()
test.instance_method()

#the same
ClassTest.instance_method(test)
ClassTest.class_method()
ClassTest.static_method()
