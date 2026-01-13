import sys

h,w = map(int,sys.stdin.readline().split())
height = list(map(int,sys.stdin.readline().split()))
ans = 0
for i in range(1,w-1):
    left_max = max(height[:i])
    right_max = max(height[i+1:])
    water = min(left_max,right_max) - height[i]
    if water > 0:
        ans += water
print(ans)