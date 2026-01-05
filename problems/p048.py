import sys

n,m = map(int,sys.stdin.readline().split())
rank1 = []
rank2 = []

for i in range(1,n+1):
    rank = int(sys.stdin.readline().strip())
    rank1.insert(rank-1,i)

second_player = []
second_player = rank1[:m]

for j in range(m):
    player = second_player[m-1-j]
    rank = int(sys.stdin.readline().strip())
    rank2.insert(rank-1, player)

for k in range(3):
    print(rank2[k])
    
    