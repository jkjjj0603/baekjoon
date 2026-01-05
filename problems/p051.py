import sys
0
for line in sys.stdin:
    cnt = 0
    n,m = map(int,line.split())
    for i in range(n,m+1):
        s = str(i)
        x = set(s)
        if len(s) == len(set(x)):
            cnt += 1
    print(cnt)
