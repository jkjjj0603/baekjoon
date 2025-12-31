import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    streak = 0
    score = 0
    s = sys.stdin.readline().strip()
    for i in s:
        if i == "O":
            streak += 1
            score += streak
        elif i == "X":
            streak = 0
    print(score)
