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


def test_better(val, my_list: list = None):
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

print("args order-----------")

def function(a,b=1,*args, c, d=20 ,**kwargs):
    print(f"a: {a}, b: {b}, args: {args} , c:{c}, d: {d} , kwargs: {kwargs}")

function(1,2,3,4,c=44) #a: 1, b: 2, args: (3, 4) , c:44, d: 20 , kwargs: {}
function(1,2,c=3) #a: 1, b: 2, args: () , c:3, d: 20 , kwargs: {}
function(1,2,3,c=4) #a: 1, b: 2, args: (3,) , c:4, d: 20 , kwargs: {}
function(1,2,3,4,c=6) #a: 1, b: 2, args: (3, 4) , c:6, d: 20 , kwargs: {}
function(1,2,3,k1=1,k2=2,c=88) #a: 1, b: 2, args: (3,) , c:88, d: 20 , kwargs: {'k1': 1, 'k2': 2}


def test(a, *args, b):
    print(a, args, b)

# test(1, 2, 3) # typeerror
test(1, 2, b=3) #1 (2,) 3

def check(*args, **kwargs):
    print(args, kwargs)

check(*[1,2], **{'x':3}) # (1,2) {'x':3}

def master(a,b,/,c,d=10,*args,e,f=20,**kwargs):
    print(a,b,c,d,args,e,f,kwargs)

master(1,2,3,4,5,e=6,x=7) #1 2 3 4 (5,) 6 20 {'x': 7}

def master(a,d=10,*args,e,f=20):
    pass