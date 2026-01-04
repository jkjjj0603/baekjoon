import sys

height = []
for _ in range(9):
    height.append(int(sys.stdin.readline().strip()))

total = sum(height)
fake = total - 100
result = []

for i in range(9):
    found = False
    for j in range(i+1,9):
        if height[i] + height[j] == fake:
            for k in range(9):
                if k != i and k != j:
                    result.append(height[k])
            found = True
            break
    if found == True:
        break

result.sort()
for i in range(7):
    print(result[i])
 