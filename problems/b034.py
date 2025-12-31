import sys

nums = list(map(int,sys.stdin.readline().split()))

x = 1

while True:
    cnt = 0
    for num in nums:
        if x % num == 0:
            cnt += 1
    if cnt >= 3:
        print(x)
        break
    x += 1

