import sys

a = sys.stdin.readline().strip()
op = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

la = len(a)
lb = len(b)

if op == "*":
    print("1"+"0" * (la + lb -2))

elif op == "+":
    if la == lb:
        print("2"+"0"*(la - 1))
    elif la > lb:
        print("1"+"0"*(la - lb - 1)+"1"+"0"*(lb-1))
    elif lb > la:
        print("1"+"0"*(lb-la-1)+"1"+"0"*(la-1))
    