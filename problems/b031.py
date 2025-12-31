import sys

t = int(sys.stdin.readline().strip())



for _ in range(t):
    n = int(sys.stdin.readline().strip())
    best_name = ""
    best_value = -1
    for _ in range(n):
        name, value = sys.stdin.readline().split()
        value = int(value)

        if best_value < value:
            best_value = value
            best_name = name
    print(best_name) 

