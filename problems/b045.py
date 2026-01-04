import sys

arr = []
top5 = []
total = 0
idxs = []

for i in range(1,9):
    score = int(sys.stdin.readline().strip())
    arr.append((score,i))

arr.sort(key = lambda x : x[0], reverse = True)
top5 = arr[:5]

for num,_ in top5:
    total += num

for _,idx in top5:
    idxs.append(idx)
    idxs.sort()

print(total)

for i in range(0,5):
    print(idxs[i],end = " ")

