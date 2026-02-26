import sys

n = int(sys.stdin.readline().strip())

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

c1 = s1.count("w")
c2 = s2.count("w")

if c1 > c2:
    print("Oryang")
elif c1 < c2:
    print("Manners maketh man")
elif s1 == s2:
    print("Good")
else:
    print("Its fine")