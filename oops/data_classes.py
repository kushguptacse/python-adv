from dataclasses import dataclass, field, fields

@dataclass
class User:
    name: str
    age: int

u1 = User('kush',10)
print(u1) #User(name='kush', age=10)

for f in fields(User):
    print(f"{f.name}, {f.type}") 

#print   
#name, <class 'str'>
#age, <class 'int'>

@dataclass
class Account:
    name: str
    tags: list = field(default_factory=list) # now all object will have there own list instance.

@dataclass(slots=True)
class User2: # now , no new dynamic attribute can be added in the User2 class instance
    name: str


u1 = User('lll',23)
u1.job="cricket"

u2= User2('kush')
# u2.job="it" #give error that job attribute does not exists