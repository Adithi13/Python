#Enter a string of length N indexed 0 to N-1. Print even-indexed character and odd-indexed character as per 2 space seperated strings on a single line [0 is the even index]
CODE:
# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range (0 , T):
    S = input()
    print(S[0::2] + " " + S[1::2])
