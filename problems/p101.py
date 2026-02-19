import sys

n = int(sys.stdin.readline().strip())
req = list(map(int,sys.stdin.readline().split()))
used = set()
reject = 0
for seat in req:
    if seat in used:
        reject += 1
    else:
        used.add(seat)
print(reject)