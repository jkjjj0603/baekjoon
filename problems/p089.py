import sys

t,s = map(int,sys.stdin.readline().split())

if s == 1:
    print(280)
elif 12 <= t <= 16:
    print(320)
else:
    print(280)