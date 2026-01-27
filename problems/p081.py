import sys
from itertools import permutations

n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))
best = 0

for p in permutations(arr):
    score = 0
    for i in range(n-1):
        score += abs(p[i] - p[i+1])
    best = max(best,score)
print(best)