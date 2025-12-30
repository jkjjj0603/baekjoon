import sys
t = int(sys.stdin.readline().strip())

for _ in range(t):
    parts = sys.stdin.readline().split()
    num = float(parts[0])

    for op in parts[1:]:
        if op == "@":
            num *= 3
        elif op == "%":
            num += 5
        elif op == "#":
            num -= 7

    print(f"{num:.2f}")    