import sys
n = int(sys.stdin.readline().strip())

cute_cnt = 0
not_cnt = 0

for _ in range(n):
    op = int(sys.stdin.readline().strip())
    if op == 1:
        cute_cnt += 1
    elif op == 0:
        not_cnt += 1
if cute_cnt > not_cnt:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")