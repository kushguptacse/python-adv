# special methods with double underscore  like __init__


class Number:
    def __init__(self, a):
        self._a = a

    def __add__(self, b):
        return Number(self._a + b._a)

    def __str__(self):
        return f"{self._a}"

    def __eq__(self, value):
        return self._a == value._a


a = Number(10)  # call init method
b = Number(10)  # call init method
c = a + b  # call add method
print(c)  # call str method and print 20
print(a == b)  # call eq method and print True


class Greeter:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f"Hello {self.name}")


g = Greeter("Kush")
g()  # print Hello Kush

print("----------------------__new__----------------------------")

class Dummy:
    def __new__(cls, *args, **kwargs):
        print("creating new object")
        return super().__new__(cls)

    def __init__(self, name):
        print(f"inside init {name}")
        self.name = name

Dummy("kush") # print creating new object first and inside init kush later

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            print("Object already exists")
        else:
            cls._instance = super().__new__(cls)
        return cls._instance


print(id(Singleton())) #128446005197216
print(id(Singleton()))  #128446005197216
