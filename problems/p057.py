import sys

n = int(sys.stdin.readline().strip())
five = n // 5
ans = 0

while True:
    rem = n - five * 5
    if rem % 3 == 0:
        three = rem // 3
        ans = five + three
        print(ans)
        break
    else:
        print(-1)
        break

