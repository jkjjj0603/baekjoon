import sys

b = sys.stdin.readline().strip()

height = 10

for i in range(1,len(b)):
    if b[i] == b[i-1]:
        height = height + 5
    elif b[i] != b[i-1]:
        height = height + 10

print(height)

