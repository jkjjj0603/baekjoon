import sys

n = int(sys.stdin.readline().strip())
divisors = list(map(int, sys.stdin.readline().split()))
print(min(divisors) * max(divisors))