import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
target_lst = list(map(int,sys.stdin.readline().split()))

dq = deque(range(1,n+1))
moves = 0

for target in target_lst:
    idx = dq.index(target)
    left = idx
    right = len(dq) - idx

    if left <= right:
        for i in range(left):
            x = dq.popleft()
            dq.append(x)
            moves += 1

    elif right < left:
        for i in range(right):
            x = dq.pop()
            dq.appendleft(x)
            moves += 1
    
    dq.popleft()
print(moves)
