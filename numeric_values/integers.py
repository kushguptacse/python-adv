import sys

my_val = 255
print(f"size: {sys.getsizeof(my_val)} bytes")  # size: 28 bytes
my_val = 2**64
print(f"size: {sys.getsizeof(my_val)} bytes")  # size: 36 bytes


#convert float to int
print(int(2.3)) #2
print(int(2.5)) #2
print(int(2.9)) #2
print(int(-2.9)) #-2

#binary
my_binary3 = 0b101010
print(f"Value: {my_binary3}")#Value: 42

hex_num = 0xA
print(f"Value: {hex_num}") #Value: 10