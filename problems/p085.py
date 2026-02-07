import sys

n = int(sys.stdin.readline())

for _ in range(n):
    line = sys.stdin.readline().rstrip('\n')

    if line:
        line = line[0].upper() + line[1:]
    print(line)

