import sys

a,b = map(int,sys.stdin.readline().split())
n = int(sys.stdin.readline().strip())
ans = abs(a-b)

for _ in range(n):
    x = int(sys.stdin.readline().strip())
    button = 1 + abs(x - b)
    if ans > button:
        ans = button
print(ans)