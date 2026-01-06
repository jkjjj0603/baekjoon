import sys
from collections import deque

n = int(sys.stdin.readline().strip())
dq = deque()

for _ in range(n):
    command = sys.stdin.readline().strip()

    if command.startswith("push_front"):
        cmd_lst = command.split()
        dq.appendleft(int(cmd_lst[1]))
    elif command.startswith("push_back"):
        cmd_lst = command.split()
        dq.append(int(cmd_lst[1]))
    elif command == "pop_front":
        if len(dq) != 0:
            num = dq.popleft()
            print(num)
        elif len(dq) == 0:
            print(-1)
    elif command == "pop_back":
        if len(dq) != 0:
            num = dq.pop()
            print(num)
        elif len(dq) == 0:
            print(-1)
    elif command == "size":
        print(len(dq))
    elif command == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif command == "front":
        if len(dq) != 0:
            print(dq[0])
        elif len(dq) == 0:
            print(-1)
    elif command == "back":
        if len(dq) != 0:
            print(dq[-1])
        elif len(dq) == 0:
            print(-1)


    
