import sys

n = int(sys.stdin.readline().strip())

room = []
for _ in range(n):
    line = sys.stdin.readline().strip()
    room.append(line)

row_cnt = 0
col_cnt = 0

for i in range(n):
    length = 0
    for j in range(n):
        if room[i][j] == ".":
            length += 1
        elif room[i][j] == "X":
            if length >= 2:
                row_cnt += 1
            length = 0
    if length >= 2:
        row_cnt += 1

for i in range(n):
    length = 0
    for j in range(n):
        if room[j][i] == ".":
            length += 1
        elif room[j][i] == "X":
            if length >=2:
                col_cnt += 1
            length = 0
    if length >= 2:
        col_cnt += 1

print(f"{row_cnt} {col_cnt}")
    
