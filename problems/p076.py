import sys

n = int(sys.stdin.readline().strip())
cnt = {}
for _ in range(n):
    filename = sys.stdin.readline().strip()
    name, ext = filename.rsplit(".",1)
    if ext in cnt:
        cnt[ext] += 1
    else:
        cnt[ext] = 1
for ext in sorted(cnt):
    print(ext, cnt[ext])
    
