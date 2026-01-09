import sys

cnt = 0
last = {}

n = int(sys.stdin.readline().strip())

for _ in range(n):
    cow,pos = map(int,sys.stdin.readline().split())
    if cow in last:
        prev = last[cow]
        if prev != pos:
            cnt += 1
            last[cow] = pos
        else:
            last[cow] = pos
    else:
        last[cow] = pos
    

print(cnt)
