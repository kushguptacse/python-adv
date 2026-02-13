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
