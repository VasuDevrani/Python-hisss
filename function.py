import math

# prints all function in math library
print(dir(math))
print(math.sqrt(16))

# direct import a particular function
from math import tan
print(tan(16))

# user defined functions
def print_sum(first, second = 2):
    print(first + second)

print_sum(1, 4)