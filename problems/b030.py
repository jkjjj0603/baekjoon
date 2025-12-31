import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    y_sum = 0
    k_sum = 0

    for _ in range(9):
        y, k = map(int, sys.stdin.readline().split())
        y_sum += y
        k_sum += k

    if y_sum > k_sum:
        print("Yonsei")
    elif y_sum < k_sum:
        print("Korea")
    else:
        print("Draw")

