import sys

n,l,d = map(int,sys.stdin.readline().split())

total = n * l + (n -1) * 5
t = 0

while total > t:
    call = t % (l + 5)
    if call >= l:
        print(t)
        sys.exit(0)
    t += d
print(t)