#Given a array of length N, the task is to print the array in reversed order. ie, Input:[1,2,3,4] Expected Output is:[4,3,2,1]
CODE:
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
for i in reversed(arr):
    print(i,end=' ')
