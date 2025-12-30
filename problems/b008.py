import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
    r, s = sys.stdin.readline().split()
    r = int(r)
    out = []
    for ch in s:
        out.append( ch * r)
    print("".join(out))