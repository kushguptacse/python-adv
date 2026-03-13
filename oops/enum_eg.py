from enum import Enum
from enum import IntEnum
from enum import auto


class Colors(Enum):
    RED = 1
    GREEN = "hello"
    BLUE = 3


print(Colors.GREEN.value)  # hello
print(issubclass(Colors, int))  # False


class Colors2(IntEnum):
    RED = 1
    # GREEN = "hello" #not allowed
    GREEN = 2
    BLUE = 3


print(Colors2.GREEN.value)  # 2
print(issubclass(Colors2, int))  # True

def switch_case_enum(v):
    match v:
        case Colors2.RED:
            print(v)
        case Colors2.BLUE:
            print("Color :", v)
        case Colors2.GREEN:
            print("another: ", v)
        case _:
            print("wrong color")

switch_case_enum(2) #another:  2
switch_case_enum(Colors2.RED) #Colors2.RED
switch_case_enum(8) #wrong color

class Colors3(Enum):
    RED = auto() # python assign number from 1 as enum values
    GREEN = auto()
    BLUE = auto()


print(Colors3.GREEN.value)  # 2
print(list(Colors3))  # [<Colors3.RED: 1>, <Colors3.GREEN: 2>, <Colors3.BLUE: 3>]


