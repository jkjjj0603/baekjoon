import sys
from collections import deque

n,w,l= map(int,sys.stdin.readline().split())
truck_lst = list(map(int,sys.stdin.readline().split()))

bridge = deque([0]*w)
time = 0
bridge_weight = 0
idx = 0

while True:
    time += 1
    out = bridge.popleft()
    bridge_weight -= out

    if idx < n and bridge_weight + truck_lst[idx] <= l:
        bridge.append(truck_lst[idx])
        bridge_weight += truck_lst[idx]
        idx += 1
    
    else:
        bridge.append(0)

    if idx == n and bridge_weight == 0:
        break
print(time)