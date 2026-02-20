import sys

h = sys.stdin.readline().strip()
n = sys.stdin.readline().strip()
cnt = 0
len_h = len(h)
len_n = len(n)

for i in range(0,len_h - len_n + 1):
    if h[i:i+len_n] == n:
        cnt += 1
print(cnt)