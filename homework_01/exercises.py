"""
Implementation of coding tasks 2.2 to 2.4
"""

import numpy as np

# 2.2 LIST COMPREHENSION
# list of squares of all numbers between 0 and 100
print([i**2 for i in range(101)])
# now list only the even squared numbers
print([i**2 for i in range(101) if i**2 % 2 == 0])

# 2.3 GENERATORS
# a function which returns "meow" twice as many times as before with every consecutive call
def meow(limit):
    for i in range(limit):
        yield 2**i*"meow "
# create a generator object
obj = meow(100)
# test the generator
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

# 2.4 NUMPY
# create a 5x5 array with normally distributed numbers
arr = np.random.normal(0, 1, (5,5))
# function to replace array elements with their squares (if greater than 0.09) or 42
replace = np.vectorize(lambda x: x**2 if x > 0.09 else 42, otypes=[float])
# apply the function to our array
arr = replace(arr)
# print the fourth column
print(arr[:, 3])
