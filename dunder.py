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
print(a==b) # call eq method and print True
