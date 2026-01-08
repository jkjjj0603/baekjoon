import sys

n = int(sys.stdin.readline().strip())
arr = []

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    arr.append(num)
arr.sort()

total = sum(arr)
avg = round(total / n)
mid = arr[n//2]
freq = {}
max_freq = -1
modes = []
range_val = arr[-1] - arr[0]
m_modes = 0

for x in arr:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
max_freq = max(freq.values())

for key, value in freq.items():
    if value == max_freq:
        modes.append(key)
modes.sort()

if len(modes) == 1:
    m_modes = modes[0]
else:
    m_modes = modes[1]

print(avg)
print(mid)
print(m_modes)
print(range_val)

