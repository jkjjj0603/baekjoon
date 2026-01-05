import sys

n,b = map(int,sys.stdin.readline().split())

if n <= 2**(b+1) -1:
    print("yes")
else:
    print("no")