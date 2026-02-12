def square(a: int) -> int:
    return a**2


print(square(2))  # 4
print(square(2.0))  # still works and print 4.0as python does not stop


# it provide info that both int and float can be taken as argument and can be returned.
def square_2(a: int | float) -> int | float:
    return a**2


print(square_2(2))  # 4
print(square_2(2.0))  # 4.0

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