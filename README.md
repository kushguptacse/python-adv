# 🐍 Python-adv Notes

This document provides a concise overview of advanced Python topics like Memory, Async, Cython, etc.

---

## 🔤 Type Annotations
1. Python supports dynamic typing, which means variable types are determined at runtime.
Because of this, it can sometimes be unclear what type of arguments a function expects or what type it returns.

2. Type annotations improve readability and maintainability by indicating expected types, but they are not enforced at runtime by python.

```python
def square(a: int) -> int:
    return a**2

print(square(2))  # 4
print(square(2.0))  # still works -> 4.0 (Python does not block it)

# (Python 3.10+) Multiple possible types can be specified using `|`:
def square_2(a: int | float) -> int | float: 
    return a**2

print(square_2(2))  # 4
print(square_2(2.0)) # 4.0
```
3. Type annotations are not enforced by Python itself. Tools like mypy, pyright, or IDEs use them to detect type errors during development.

4. The `typing` module provides advanced type annotations like `List`, `Dict`, and `Optional`.

```python
from typing import List, Dict, Optional

def process(arr: List[int]) -> Dict[str, int]:
    return {"count": len(arr)}

print(process([1, 2]))  # {'count': 2}
print(process(["a"]))  # {'count': 1}

# Optional[T] means the value can be T or None.
def greet(val: Optional[str]) -> str:
    return f"Hello {val or 'Guest'}"

print(greet('kush'))  # Hello kush
print(greet(None))  # Hello Guest
print(greet(2))  # Hello 2
#print(greet())  # give error as some value is expected

def greet_without_optional(val: str | None) -> str: # same as greet but modern syntax 3.10+
    return f"Hello {val or 'Guest'}"

print(greet('kush'))  # Hello kush
print(greet(None))  # Hello Guest
```

---

## 🔤 Numeric Values - Integers

1. Python int objects are arbitrary precision (not fixed 32-bit/64-bit like C/C++/Java). They automatically grow as needed. Internally, they are full objects (PyLongObject) and store metadata along with digit data, which increases memory usage.

For example, although 1 byte (8 bits) is enough to store numbers from 0–255 in low-level languages, Python still uses more memory because every integer is an object.

Python integers do not overflow like fixed-size integers in other languages.
```python
import sys

my_val = 255
print(f"size: {sys.getsizeof(my_val)} bytes")  # size: 28 bytes
my_val = 2**64
print(f"size: {sys.getsizeof(my_val)} bytes")  # size: 36 bytes
```

2. Some useful number examples-
```python
#convert float to int
print(int(2.3)) #2
print(int(2.5)) #2
print(int(2.9)) #2
print(int(-2.9)) #-2

#binary literal
my_binary3 = 0b101010
print(f"Value: {my_binary3}")#Value: 42
#hexadecimal literal
hex_num = 0xA
print(f"Value: {hex_num}") #Value: 10
```

---

## 🔤 Numeric Values - Floats

1. C, C++, Java etc.: Float (32bits/4Byte), Double (64bits=8Byte)

Python: Float (64bits=8Byte)

sign: 1bit
exponent: 11bits
significant bits: 52bits

But if you create variable and assign a value. it will take minimum of 24 bytes (8 bytes for value and remaining 16 for class metadata)

2. Float value should not be compared using == operater as they can be different due to precision.
```python
def float_val_complete(num: float):
    print(f"value: {num:.32f}")
float_val_complete(42.09)  # value: 42.09000000000000341060513164848089
my_fraction = 1 / 10 + 1 / 10 + 1 / 10

val2 = 0.3
float_val_complete(val2) # value: 0.29999999999999998889776975374843
# conditions fail as they are not exactly same.
if my_fraction == val2: #print both are different
    print("both are same")
else:
    print("both are different")

def float_is_equal(
    x: float,
    y: float,
) -> bool:
    epsilon = 1e-15 # very small number
    difference = math.fabs(x - y) # difference of 2 numbers 
    return difference < epsilon # if diff is smaller then epsilon consider them equal

if float_is_equal(val2,my_fraction): #print both are same
    print("both are same")
else:
    print("different")
```

3. Rounding: round(number, ndigits)
If ndigits is positive → rounds to decimal places

If ndigits is zero or omitted → rounds to nearest integer

If ndigits is negative → rounds to the left of the decimal point
```python
my_float = 142.4242424242
my_float1 = round(my_float)
print(my_float1) # 142
float_val_complete(my_float1) #value: 142.00000000000000000000000000000000

my_float_rounded2 = round(my_float, 4)
print(my_float_rounded2) #142.4242
float_val_complete(my_float_rounded2) #142.42420000000001323314791079610586
```

---

## 🔤 Logical Expressions - Booleans

1. bool just like int and float are also objects. they are sub-class of int. and it take extra memory for metadata.

True  → integer value 1
False → integer value 0

```python
print(True+True)    #2
print(True*5)   #5
print(False+10)   # 10
my_bool = True
print(sys.getsizeof(my_bool))  # platform dependent (often 28)
my_bool1 = False
print(sys.getsizeof(my_bool1))  # platform dependent
print(issubclass(bool, int)) #True. bool is a subclass of int
print(isinstance(True,bool)) #True
print(isinstance(False,bool))#True
print(isinstance(False,int))#True
print(isinstance(1,bool)) #False
print(isinstance(0,bool)) #False
```

2. is vs. == operator: 'is' and 'is not' checks reference in memory and '==' and '!=' check values of two variables.

For == operator every True == 1 and False == 0

For is operator exact memory location must match, internal type convertion of int to bool will not result in True.
```python
my_bool = True
print(my_bool == 1) #True
print(my_bool == 0) #False
print(my_bool == 12)  #False

print(my_bool is True) #True
print(my_bool is  1) #False
print(my_bool is  0) #False
print(my_bool is 12)  #False
print(my_bool is None)  #False
```

3. Every object of a built-in type has a Truth Value.

An instance is True if it is not: None, False, 0, or empty list.
```python
def print_truth_value(var) -> None:
    print(bool(var))

value1 = None  # None
value2 = 0  # int
value3 = False  # bool
value4 = []  # list

print_truth_value(value1)#False
print_truth_value(value2)#False
print_truth_value(value3)#False
print_truth_value(value4)#False

value5 = 1
value6 = True
value7 = [0]
print_truth_value(2323)#True
print_truth_value(value5)#True
print_truth_value(value6)#True
print_truth_value(value7)#True
``` 

---

## 🔤 Switch Case: match
Python 3.10 introduced the match-case statement, which is similar to switch-case in languages like Java, but more powerful. It supports pattern matching, guards, destructuring, and multiple conditions
```python
def handle_data(data):
    match data:
        # guard condition
        case v if isinstance(v, int) and v < 0:
            print("Negative int:", v)
        # exact value
        case 100:
            print("Value is 100")
        # list destructuring
        case [a, b]:
            print("List:", a, b)
        # list variable unpack
        case [first, *mid, last]:
            print("Long list:", first, mid, last)
        # dict destructuring
        case {"name": name, "age": age}:
            print("User:", name, age)
        # default
        case _:
            print("Default:", data)

handle_data(-1) #Negative int: -1
handle_data(100) #Value is 100
handle_data([1, 2]) #List: 1 2
handle_data([1, 2,3,4,5,6]) #Long list: 1 [2, 3, 4, 5] 6
handle_data({"name": "Kush", "age": 25})# User: Kush 25
handle_data("kush") #Default: kush
```

---

## 🔤 Immutability 
1. In python everything is an object and variables store reference to objects. Immutable objects cannot be modified after creation, so operations like addition of two int will result in creating a new object instead of modifying existing object.
For mutable data types like list, the original object itself can be modified without creating a new object.

Immutable types: int, float, bool, str, tuple, None

Mutable types: list, dict, set, etc.

2. Python reuses some objects to save memory. like True and False will always use same memory even if created multiple times. for int values -5 to 256 will be reused to avoid object creation.

```python
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
print_memory_address(list3) # list3 is new object because + operator creates new list
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

```
3. In case of mutable object like List, Difference between l1 + l2 and l1 += l2 (Object Creation)
```python
list1 = [1, 2]  # total 3 objects: 2 int objects and 1 list object
list2 = [3, 4]  # total 3 objects: 2 int objects and 1 list object

list3 = list1 + list2  
# 1 new object created: new list object [1,2,3,4]
# No new int objects created (references reused)

list1 += list2  
# no new object created
# list1 itself modified in-place to [1,2,3,4]

```

| Operation      | New list object created | New int objects created | Total new objects created | Original l1 modified | Memory behaviour                   |
| -------------- | ----------------------- | ----------------------- | ------------------------- | -------------------- | ---------------------------------- |
| `l3 = l1 + l2` | ✅ Yes (1)               | ❌ No                    | **1**                     | ❌ No                 | Creates new list and assigns to l3 |
| `l1 += l2`     | ❌ No                    | ❌ No                    | **0**                     | ✅ Yes                | Extends existing list in-place     |

Conclusion: For mutable types like list, += modifies object in-place (no new object created).

For immutable types like int, += creates new object.

---

## 🔤 Function 
1. All parameters without default values must be defined before parameters with default values in function definition
```python
def meth(p1,p2,p3=0,p4=10,p5): # invalid, non default argument cannot come after default argument.
   print(p1,p2,p3,p4,p5)
```

2. If mutable variable is passed as default argument then it may lead to unpredictable behaviour. As, Default argument values are evaluated only once at function definition time, not at function call time.
```python
def test(val, my_list=[]):
    my_list.append(val)
    return (my_list)

print(test("k")) # ['k']
print(test("l")) #['k', 'l'] 

def test_better(val, my_list: list=None):
    if my_list is None:
        my_list = []

    my_list.append(val)
    return my_list

print(test_better("k")) # ['k']
print(test_better("l")) #['l']
```

3. Order of argument in function:  Positional or keyword parameters (with or without Default value) -> *args-> Keyword-only parameters (with or without Default value) -> **kwargs
```python
def function(a,b=1,*args, c, d=20 ,**kwargs):
    print(f"a: {a}, b: {b}, args: {args} , c:{c}, d: {d} , kwargs: {kwargs}")

function(1,2,3,4,c=44) #a: 1, b: 2, args: (3, 4) , c:44, d: 20 , kwargs: {}
function(1,2,c=3) #a: 1, b: 2, args: () , c:3, d: 20 , kwargs: {}
function(1,2,3,c=4) #a: 1, b: 2, args: (3,) , c:4, d: 20 , kwargs: {}
function(1,2,3,4,c=6) #a: 1, b: 2, args: (3, 4) , c:6, d: 20 , kwargs: {}
function(1,2,3,k1=1,k2=2,c=88) #a: 1, b: 2, args: (3,) , c:88, d: 20 , kwargs: {'k1': 1, 'k2': 2}

```

---

## 🔤 Special Parameters Function 
1. '/' and '*' : If / and * are not present in the function definition, arguments may be passed to a function by position or by keyword both.
```python
def normal(a:any)->None:
    print(a)

normal(23)
normal(a=23)
```

2. Positional-only parameters are placed before / (forward-slash). Use positional-only if you want the name of the parameters to not be available to the user.
```python
def positional(a: int, /, b: int) -> None:
    print(a,b)

positional(1, 2) # 1 2
positional(1, b=2) # 1 2
positional(a=1, b=2) # TypeError: positional() got some positional-only arguments passed as keyword arguments: 'a'
```

3. To mark parameters as keyword-only, indicating the parameters must be passed by keyword argument, place an * in the arguments list just before the first keyword-only parameter.
```python
def kwd_only_arg(*, a: int) -> None:
    print(a)

kwd_only_arg(a=1) #1
kwd_only_arg(1) #TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given
```

4. combined example-
```python
def combined_example(a: Any, /, b: Any, *, c: Any) -> None:
    print(a, b, c)

# combined_example(1, 2, 3) not allowed as c is keyword arg
combined_example(1, 2, c=3)
combined_example(1, b=2, c=3)
# combined_example(a=1, b=2, c=3) not allowed as a is positional arg

# Here e must be passed as keyword only arg, else python gives error becuase d with default value already defind before *args
def master(a,b,/,c,d=10,*args,e,f=20,**kwargs): 
    print(a,b,c,d,args,e,f,kwargs)

# once keyword argument passed, remaining args must be keyword
master(1,2,3,4,5,e=6,x=7) #1 2 3 4 (5,) 6 20 {'x': 7}
```

---

## 🔤 Closures and decorators
1.A closure is an inner function that has access to variables in the local scope of the outer function.
```python
def outer(msg: str) -> None:
    var1 = "hello"
    var2 = f"{var1} {msg}"
    def inner():
        print(var2)
    inner()

outer("kush")
```

2. decorator example with arguments passed-
```python
def debug(fn):
    def debugger(*args, **kwargs):
        print(f"Args: {args}")
        print(f"Kwargs: {kwargs}")
        print(f"Function {fn.__name__} called")
        fn_result = fn(*args, **kwargs)
        print(f"Function {fn.__name__} returns: {fn_result}")
        return fn_result

    return debugger


@debug
def something(a, b, c=0,d=4):
    return a + b if c!=0 else d

#above line is equivalent of something=debug(something)

something(1, b=2,c=3)
# Args: (1,)
# Kwargs: {'b': 2, 'c': 3}
# Function something called
# Function something returns: 3

@debug
def something2(*a, **kwargs):
    return f"{a}, {kwargs}"

something2(1,2,3,k=2)

# Args: (1, 2, 3)
# Kwargs: {'k': 2}
# Function something2 called
# Function something2 returns: (1, 2, 3), {'k': 2}
```

---

## 🔤 Difference between class, instance and static method
1. class variables are shared between all the instances of the class. Instance variables are unique for each object.
| Feature             | **Class Level Variable**                        | **Instance Variable**                           |
| ------------------- | ----------------------------------------------- | ----------------------------------------------- |
| Definition          | Variable shared by **all objects of the class** | Variable specific to **each object (instance)** |
| Where Defined       | Inside the **class**, outside methods           | Usually inside **`__init__()`** using `self`    |
| Memory Allocation   | **Single copy** shared by all instances         | **Separate copy** for each instance             |
| Access              | Accessed using **class name or object**         | Accessed using **object (`self`)**              |
| Modification Effect | Change affects **all instances**                | Change affects **only that instance**           |
| Created When        | When the **class is defined**                   | When the **object is created**                  |
| Example Use         | Constants, shared configuration                 | Object-specific data                            |

1. Instance method: They have access to class level and instance level data
```python
class Example:
    class_var = 4
    def __init__(self):
        print("inside init")
        self.ins_var = "kk"

    def ins_method(self):
        print(self.ins_var, self.class_var, Example.class_var)

print(Example.class_var)  # 4
obj = Example()  # inside init
print(obj.ins_var)  # kk
obj.ins_method()  # kk 4 4
```

2. Class method: they have access to class level data only.  
```python
class Example:
    class_var = 4
    def __init__(self):
        print("inside init")
        self.ins_var = "kk"

    @classmethod
    def class_method(cls):
        print(cls.class_var)
        #print(cls.ins_var) not available

print(Example.class_var) #4
Example.class_method() #4
obj = Example() # inside init
print(obj.ins_var) #kk
obj.class_method() #4
```

3. Static method: They are not binded to class nor to instance. they usually created inside class for utility function.
```python
class Example2:
    class_var = 4
    @staticmethod
    def static_method(arg1,arg2):
        print(arg1,arg2,Example2.class_var) 
    @staticmethod
    def static_method2():
        print("hello" )

print(Example2.class_var)  # 4
Example2.static_method(2,3)  # 2 3 4
Example2.static_method2() # hello
```
