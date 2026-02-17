from typing import Any

def print_memory_address(var: Any) -> None:
    print(hex(id(var)))

# int are immutable objects
l1 = 5
print_memory_address(l1)
l2 = 6
print_memory_address(l2)
print_memory_address(l1 + l2)  
# it will create a new object in memory as int are immutable and cannot be modified

# float are immutable objects
f1 = 2.3
print_memory_address(f1)

f2 = 2.3
print_memory_address(f2)  
# f1 and f2 may point to same object due to python optimization, but it is not guaranteed

print_memory_address(f1 + f2)  
# it will create a new object in memory as float are immutable

# list are mutable objects, but each list literal creates its own new object
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1 + list2

print_memory_address(list1)
print_memory_address(list2)
print_memory_address(list3) 
# list3 is new object because + operator creates new list

list3.append(4)
print_memory_address(list3)  # same object. List are mutable.

# bool are immutable and python uses singleton instances for True and False
my_bool1 = True
my_bool2 = True

my_bool3 = False
my_bool4 = False

print_memory_address(my_bool1) 
print_memory_address(my_bool2) # both True point to same singleton object
print_memory_address(my_bool3)
print_memory_address(my_bool4) # both False point to same singleton object

# tuple are immutable objects
my_tuple = (1, 2, 3)
print(my_tuple)
print_memory_address(my_tuple) 

my_tuple1 = (1, 2, 3)
print(my_tuple1)

print_memory_address(my_tuple1) # may point to same object due to optimization, but not guaranteed

