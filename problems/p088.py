import sys

found = []
for i in range(5):
    name = sys.stdin.readline().strip()
    if "FBI" in name:
        found.append(i + 1)
if not found:
    print("HE GOT AWAY!")
else:
    found.sort()
    print(*found)