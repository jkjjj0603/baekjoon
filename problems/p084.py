import sys

a,b,c = map(int,sys.stdin.readline().split())
total = a + b + c

if total >= 100:
    print("OK")
else:
    m = min(a,b,c)
    if m == a:
        print("Soongsil")
    elif m == b:
        print("Korea")
    elif m == c:
        print("Hanyang")
