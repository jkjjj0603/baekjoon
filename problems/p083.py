import sys

n = int(sys.stdin.readline().strip())
ans = 0

for _ in range(n):
    word = sys.stdin.readline().strip()

    seen = set()
    prev = None
    is_group = True
    
    for ch in word:
        if ch == prev:
            continue

        if prev is not None:
            seen.add(prev)

        if ch in seen:
            is_group = False
            break

        prev = ch

    if is_group:
        ans += 1

print(ans)