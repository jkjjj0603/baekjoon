import sys

n = sys.stdin.readline().strip()
cnt = [0] * 10
ans = 0

for ch in n:
    d = int(ch)

    if d == 6 or d == 9:
        cnt[6] += 1
    else:
        cnt[d] += 1 
    
sixnine = cnt[6]
cnt[6] = (sixnine + 1) // 2

ans = max(cnt)
print(ans)