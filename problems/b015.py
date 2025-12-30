import sys
s = int(sys.stdin.readline().strip())

total = 0
cnt = 0

while total + (cnt+ 1) <= s:
    cnt = cnt + 1
    total = total + cnt

print(cnt)