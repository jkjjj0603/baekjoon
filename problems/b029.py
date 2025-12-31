import sys

t = int(sys.stdin.readline().strip())
c_score = 100
s_score = 100

for _ in range(t):
    a,b = map(int,sys.stdin.readline().split())
    if a > b:
        s_score = s_score - a
    elif a < b:
        c_score = c_score - b
print(c_score)
print(s_score)
