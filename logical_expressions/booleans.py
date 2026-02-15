import sys

my_bool = True
print(sys.getsizeof(my_bool))  # 28
my_bool1 = False
print(sys.getsizeof(my_bool1))  # 24

print(issubclass(bool, int)) #True. bool is a subclass of int

print(isinstance(True,bool)) #True
print(isinstance(False,bool))#True

print(isinstance(1,bool)) #False
print(isinstance(0,bool)) #False


print("is vs ==")
my_bool = True
print(my_bool == 1) #True
print(my_bool == 0) #False
print(my_bool == 12)  #False

print(my_bool is True) #True
print(my_bool is  1) #False
print(my_bool is  0) #False
print(my_bool is 12)  #False
print(my_bool is None)  #False

# check type converstion
print("****************")

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