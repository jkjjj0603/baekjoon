import sys

n = int(sys.stdin.readline().strip())
people = []
ranks = []

for _ in range(n):
    w, h = map(int,sys.stdin.readline().split())
    people.append((w,h))
for i in range(n):
    rank = 1
    for j in range(n):
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            rank += 1
    ranks.append(rank)

print(" ".join(map(str, ranks)))
        