import sys

n,m = map(int,sys.stdin.readline().split())

not_heard = set()
not_seen = set()
inter = set()

for _ in range(n):
    name = sys.stdin.readline().strip()
    not_heard.add(name)

for _ in range(m):
    name = sys.stdin.readline().strip()
    not_seen.add(name)

inter = not_heard.intersection(not_seen)
result = sorted(inter)

cnt = 0

for i in result:
    cnt += 1

print(cnt)
for j in result:
    print(j)