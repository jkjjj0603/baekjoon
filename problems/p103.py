import sys

n,m = map(int,sys.stdin.readline().split())

if m * 100 >= n * 81:
    print("yaho")
else:
    print("no")