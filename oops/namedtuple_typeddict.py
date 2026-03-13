from typing import NamedTuple, TypedDict
from collections import namedtuple

class Animal(NamedTuple):
    name: str
    age: int

a = Animal("Bruno",3)
print(a) #Animal(name='Bruno', age=3)

a1 = namedtuple("AnimalTest", ["name","age"])
animal_obj = a1("Bruno",4)
print(animal_obj) #Animal2(name='Bruno', age=4)


class User(TypedDict):
    name: str
    age: int

u1: User = {"name": "Jan", "age": 28, "is_admin": True}
print(u1)