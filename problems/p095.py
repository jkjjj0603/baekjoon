import sys

a,b = map(int,sys.stdin.readline().split())

win = {(0,2),(2,5),(5,0)}
valid = {0,2,5}

a_invalid = a not in valid
b_invalid = b not in valid

if a_invalid and b_invalid:
    print("=")
elif a_invalid:
    print("<")
elif b_invalid:
    print(">")
else:
    if (a,b) in win:
        print(">")
    elif (b,a) in win:
        print("<")
    else:
        print("=")
