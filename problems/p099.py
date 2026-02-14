import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))
cnt = 0

for i in range(n):
    if arr[i] != i + 1:
        cnt += 1
print(cnt)