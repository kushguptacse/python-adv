import sys, math

print(sys.getsizeof(42.09))  # 24


def float_val_complete(num: float):
    print(f"value: {num:.32f}")


float_val_complete(42.09)  # value: 42.09000000000000341060513164848089
my_fraction = 1 / 10 + 1 / 10 + 1 / 10
float_val_complete(my_fraction)

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
print("**********************************************************")
# rounding
my_float = 142.4242424242
my_float1 = round(my_float)
print(my_float1) # 142
float_val_complete(my_float1) #value: 142.00000000000000000000000000000000

my_float_rounded2 = round(my_float, 4)
print(my_float_rounded2) #142.4242
float_val_complete(my_float_rounded2) #142.42420000000001323314791079610586

my_float_rounded2 = round(my_float, -3)
print(my_float_rounded2) # 0.0
float_val_complete(my_float_rounded2) #value: 0.00000000000000000000000000000000

my_float_rounded2 = round(my_float, -2)
print(my_float_rounded2) # 100.0
float_val_complete(my_float_rounded2) #value: 100.00000000000000000000000000000000

my_float_rounded2 = round(my_float, -1) 
print(my_float_rounded2)# 140.0
float_val_complete(my_float_rounded2) #value: 140.00000000000000000000000000000000