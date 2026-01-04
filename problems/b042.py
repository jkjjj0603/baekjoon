import sys

s = sys.stdin.readline().strip()
n = len(s)
a = ""
b = ""
c = ""
candidate = ""
best = None

for i in range(1,n-1):
    for j in range(i+1,n):
        a = s[:i]
        b = s[i:j]
        c = s[j:]

        ra = a[::-1]
        rb = b[::-1]
        rc = c[::-1]

        candidate = ra + rb + rc
        if best is None or best > candidate:
            best = candidate
            
print(best)



    
       