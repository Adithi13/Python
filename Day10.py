#Given a base 10 integer n, convert it to binary(base 2).Find and print the base 10 integer denoting the maximum number of consecutive 1's in n's binary representation.
CODE:
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    
    list = []
    
    
    while n > 0:
        ans = n % 2
        n = n//2
        list.append(ans)
    
    count = 0
    maximum = 0

    for bit in list:
        
        if bit == 1:
            count += 1
            
            if count > maximum:
                maximum = count
        
        else:
            count = 0

    print(maximum)
