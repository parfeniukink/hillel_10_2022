class Person:
    @classmethod
    def hello(cls):
        print("Hello")


john = Person()
john.hello()

Person.hello()
