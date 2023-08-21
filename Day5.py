#Given an integer, n print its first 10 multiples. Each multiple n X i (where 1<= i <=10)should be printed on a new line in the form: n x i = result.
CODE:
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
for i in range(1,11):
    result = n*i  # or     s = n * i
print(f"{n} X {i} = {result}") # or  print(n,"x",i,"=",s)
