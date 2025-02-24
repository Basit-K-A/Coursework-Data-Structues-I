"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-10"
------------------------------------------------------------------------
"""
from Stack_array import Stack
from functions import stack_reverse

source1 = Stack()

v = [8,12,8,5]
for i in range(len(v)):
    source1.push(v[i])
    
for s in source1:
    print(s)

print(stack_reverse(source1))




