#Given n names and phone nos, assemble a phone book that maps friends' names to their respective phone. For each name queried, print the associatedentry from your phone book on a new line in the form name=phoneNumber;if an entry for name is not found, print Not found instead.
CODE:
n = int(input())
phoneBook = {}


for i in range(0, n):
  x = str(input()).split(" ")
  name = x[0]
  number = x[1]  
  phoneBook[name] = number

  
while True:
    try:
        name = input()
    except:
        break
    if name in phoneBook:
        number = phoneBook[name]
        print(name + "=" + number)
    else:
        print("Not found")
