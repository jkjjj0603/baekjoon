import sys

s = sys.stdin.readline().strip()
s = s.upper()
cnt = [0] * 26
mx = 0

for ch in s:
    idx = ord(ch) - ord("A")
    cnt[idx] += 1

mx = max(cnt)

if cnt.count(mx) >= 2:
    print("?")
else:
    print(chr(cnt.index(mx) + ord("A")))