import sys

n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

b = s.count("B")
r = s.count("R") // 2
o = s.count("O")
n = s.count("N")
z = s.count("Z")
e = s.count("E") // 2
s_ = s.count("S")
i = s.count("I")
l = s.count("L")
v = s.count("V")

print(min(b,r,o,n,z,e,s_,i,l,v))