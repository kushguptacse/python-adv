import sys

my_val = 255
print(f"size: {sys.getsizeof(my_val)} byte")  # size: 28 byte
my_val = 2**64
print(f"size: {sys.getsizeof(my_val)} byte")  # size: 36 byte
