import sys

s = sys.stdin.readline().strip()

rev = s[::-1]

if s == rev:
    print(1)
else:
    print(0)