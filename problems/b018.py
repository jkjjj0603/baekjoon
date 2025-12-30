import sys

a,b,c = map(int,sys.stdin.readline().split())
price = 0
if a == b == c:
    price = 10000 + a * 1000
    print(price)
elif a == b or a == c:
    price = 1000 + a * 100
    print(price)
elif b == c:
    price = 1000 + b * 100
    print(price)
else:
    price = max(a,b,c) * 100
    print(price)
    