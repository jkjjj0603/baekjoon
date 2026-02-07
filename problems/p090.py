import sys

n,m = map(int,sys.stdin.readline().split())
arr = []

for num in range(1,n+1):
    arr.append(num)

for _ in range(m):
    i,j,k = map(int,sys.stdin.readline().split())
    left = arr[:i-1]
    mid1 = arr[i-1:k-1]
    mid2 = arr[k-1:j]
    right = arr[j:]
    arr = left + mid2 + mid1 + right
print(*arr)