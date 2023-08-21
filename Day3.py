#Given an integer n to perfom conditional actions: if n is odd print Weird, if it is even & in range 2-5 then Not weird, if in range 6-20 Weird and if >20 then Not Weird.
CODE:
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input().strip())
if N%2 != 0:
        print("Weird")
else:
    if N>=2 and N<5:
            print("Not Weird")
    
    if N>=6 and N<=20:
            print("Weird")
    
    if N>20:
        print("Not Weird")

    
