import sys

n = int(sys.stdin.readline().strip())
five = n // 5
ans = 0
found = False

while five >= 0:
    rem = n - five * 5
    if rem % 3== 0:
        three = rem // 3
        ans = five + three
        print(ans)
        found = True
        break
    five -= 1

if not found:
    print(-1)


