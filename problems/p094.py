import sys

a,b = sys.stdin.readline().split()
la = len(a)
lb = len(b)
l = max(la,lb)
res = ""

if la != lb:
    a = a.zfill(l)
    b = b.zfill(l)

for i in range(l):
    c = int(a[i]) + int(b[i])
    res += str(c)
print(res)