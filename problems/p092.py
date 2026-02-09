import sys

n = int(sys.stdin.readline().strip())

num = len(str(n))
cnt = 0

while True:
    n = n * 2
    snum = len(str(n))
    if num < snum:
        break
    cnt += 1
print(cnt)