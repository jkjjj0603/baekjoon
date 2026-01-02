import sys

n,m = map(int,sys.stdin.readline().split())
castle = [sys.stdin.readline().strip() for _ in range(n)]

row_guard = [False] * n 
col_guard = [False] * m 

for i in range(n): 
    for j in range(m):
        if castle[i][j] == "X": 
            row_guard[i] = True 
            col_guard[j] = True

empty_rows = row_guard.count(False)
empty_cols = col_guard.count(False)

print(max(empty_rows, empty_cols))
