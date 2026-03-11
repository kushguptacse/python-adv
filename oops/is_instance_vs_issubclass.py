class Animal:
    pass
class Dog(Animal):
    pass
d = Dog()

print(isinstance(d,Animal)) # True
print(isinstance(Dog,Animal)) # False as Dog class not instance of Animal
print(issubclass(Dog,Animal))# True as Dog is subclass of animal
#print(issubclass(d,Animal))# wont allowed
print(type(d)==Dog)# True
print(type(d)==Animal)# False
print(type(Dog)==Dog)# False
print(type(Animal)==Dog)# False