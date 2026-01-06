import sys

n,l = map(int,sys.stdin.readline().split())
lights = []

for _ in range(n):
    d,r,g = map(int,sys.stdin.readline().split())
    lights.append((d,r,g))

pos = 0
t= 0

for d,r,g in lights:
    t = t + d - pos
    pos = d
    cycle = r + g
    phase = t % cycle
    if phase < r:
        t += (r - phase)
    
t += (l-pos)
print(t)