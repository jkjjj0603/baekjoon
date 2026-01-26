import sys

board = []
pos = {}

for i in range(5):
    row = list(map(int,sys.stdin.readline().split()))
    for j in range(5):
        val = row[j]
        pos[val] = (i,j)
    board.append(row)

calls = []

for _ in range(5):
    c_row = list(map(int,sys.stdin.readline().split()))
    calls.extend(c_row)

for k,x in enumerate(calls,start = 1):
    r,c = pos[x]
    board[r][c] = 0
    cnt = 0
    for i in range(5):
        if all(v == 0 for v in board[i]):
            cnt += 1
    for j in range(5):      
        if all(board[rr][j] == 0 for rr in range(5)):
            cnt += 1
    if all(board[r][r] == 0 for r in range(5)):
        cnt += 1
    if all(board[r][4-r] == 0 for r in range(5)):
        cnt += 1
    if cnt >= 3:
        print(k)
        break