from typing import Any, Optional


def meth(p1, p2, p3=0, p4=10):
    print(p1, p2, p3, p4)


meth(1, 2)

# def meth(p1,p2,p3=0,p4=10,p5): # invalid, non default argument cannot come after default argument.
#     print(p1,p2,p3,p4,p5)


def test(val, my_list=[]):
    my_list.append(val)
    return my_list


print(test("k"))  # ['k']
print(test("l"))  # ['k', 'l']

# better way


def test_better(val, my_list: Optional[list] = None):
    if my_list is None:
        my_list = []

    my_list.append(val)
    return my_list


print(test_better("k"))  # ['k']
print(test_better("l"))  # ['l']


def normal(a: any) -> None:
    print(a)


normal(23)
normal(a=23)


def positional(a: int, /, b: int) -> None:
    print(a,b)

positional(1, 2) # 1 2
positional(1, b=2) # 1 2
# positional(a=1, b=2) # TypeError: positional() got some positional-only arguments passed as keyword arguments: 'a'

def kwd_only_arg(*, a: int) -> None:
    print(a)

kwd_only_arg(a=1) #1
#kwd_only_arg(1) #TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given

def combined_example(a: Any, /, b: Any, *, c: Any) -> None:
    print(a, b, c)

# combined_example(1, 2, 3) not allowed as c is keyword arg
combined_example(1, 2, c=3)
combined_example(1, b=2, c=3)
# combined_example(a=1, b=2, c=3) not allowed as a is positional arg