import sys

n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

lower = "roygbiv"
upper = "ROYGBIV"
lower_ok = True
upper_ok = True

for ch in lower:
    if ch not in s:
        lower_ok = False

for ch in upper:
    if ch not in s:
        upper_ok = False

if lower_ok and upper_ok:
    print("YeS")
elif lower_ok:
    print("yes")
elif upper_ok:
    print("YES")
else:
    print("NO!")