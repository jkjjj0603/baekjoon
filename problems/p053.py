import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    a = float(sys.stdin.readline().strip())
    x = a / 6
    print(f"{x:.10f}")