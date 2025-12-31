import sys

n = int(sys.stdin.readline().strip())
origin = n
cnt = 0

while True:
    a = n // 10
    b = n % 10
    s = a + b

    n = (b*10) + (s%10)
    cnt += 1

    if origin == n:
        break
print(cnt)