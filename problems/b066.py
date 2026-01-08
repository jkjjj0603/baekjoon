import sys

doc = sys.stdin.readline().rstrip("\n")
word = sys.stdin.readline().rstrip("\n")

n = len(doc)
m = len(word)

i = 0
cnt = 0

while i <= n - m:
    if doc[i:i+m] == word:
        cnt += 1
        i += m
    else:
        i += 1

print(cnt)
