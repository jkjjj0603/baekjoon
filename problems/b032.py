import sys

k = int(sys.stdin.readline().strip())

divs = list(map(int,sys.stdin.readline().split()))

divs.sort()

print(divs[0]*divs[-1])
