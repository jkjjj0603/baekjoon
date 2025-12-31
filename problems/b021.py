import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    r,e,c = map(int,sys.stdin.readline().split())
    price = e - c
    if price > r:
        print("advertise")
    elif price == r:
        print("does not matter")
    elif price < r:
        print("do not advertise")

        