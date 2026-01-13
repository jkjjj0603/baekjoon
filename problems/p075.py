import sys

n = int(sys.stdin.readline().strip())
switches = [0] + list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
for _ in range(m):
    gender,num = map(int,sys.stdin.readline().split())
    if gender == 1:
        for i in range(num,n +1,num):
            switches[i] = 1 - switches[i]
    elif gender == 2:
        left = num - 1
        right = num + 1
        while left >= 1 and right <= n and switches[left] == switches[right]:
            left -= 1
            right += 1
        for i in range(left + 1 , right):
            switches[i] = 1 - switches[i]
for i in range(1, n+1):
    print(switches[i],end = " ")
    if i % 20 == 0:
        print()
