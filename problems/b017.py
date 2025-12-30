import sys

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

i = int(sys.stdin.readline().strip())

for _ in range(i):
    a , b = map(int,sys.stdin.readline().split())
    g = gcd(a,b)
    l = a * b // g
    print(l)

