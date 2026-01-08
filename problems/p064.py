import sys
from collections import deque

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n,m = map(int,sys.stdin.readline().split())
    priorities = list(map(int,sys.stdin.readline().split()))

    dq = deque()
    print_cnt = 0

    for i in range(n):
        is_target = (i == m)
        dq.append((priorities[i],is_target))

    while dq:
        p,is_target = dq.popleft()
        max_priority = -1
        for priority,_ in dq:
            if max_priority < priority:
                max_priority = priority

        if p > max_priority or p == max_priority:
            print_cnt += 1
            if is_target == True:
                print(print_cnt)
                break
        elif p < max_priority:
            dq.append((p,is_target))