
from typing import Optional


def meth(p1,p2,p3=0,p4=10):
    print(p1,p2,p3,p4)

meth(1,2)

# def meth(p1,p2,p3=0,p4=10,p5): # invalid, non default argument cannot come after default argument.
#     print(p1,p2,p3,p4,p5)

def test(val, my_list=[]):
    my_list.append(val)
    return (my_list)

print(test("k")) # ['k']
print(test("l")) #['k', 'l']

# better way

def test_better(val, my_list: Optional[list]=None):
    if my_list is None:
        my_list = []

    my_list.append(val)
    return my_list

print(test_better("k")) # ['k']
print(test_better("l")) #['l']