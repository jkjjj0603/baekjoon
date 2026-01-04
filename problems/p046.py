import sys

n,m = map(int,sys.stdin.readline().split())
j = int(sys.stdin.readline().strip())
left = 1
right = m
move = 0

for _ in range(j):
    x = int(sys.stdin.readline().strip())
    if left <= x and x <= right:
        pass
    elif x < left:
        dist = left - x
        move += dist
        left = x
        right = left + m - 1
    elif x > right:
        dist = x - right
        move += dist
        right = x
        left = right - m + 1

print(move)