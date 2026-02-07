import sys

n = int(sys.stdin.readline().strip())
k = 1
sec = 0

while n > 0:
    if n < k:
        k = 1
    n -= k
    sec += 1
    k += 1
print(sec)