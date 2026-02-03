import sys

t = int(sys.stdin.readline().strip())
scores = list(map(int, sys.stdin.read().split()))
scores = scores[:t]  


while len(scores) < 5:
    scores.append(0)

kor, math, eng, sci, lang2 = scores
a = 0
b = 0
c = 0
ans = 0

if kor > eng:
    a = (kor - eng) * 508
else:
    a = abs(kor - eng) * 108
if math > sci:
    b = (math - sci) * 212
else:
    b = abs(sci - math) * 305
if lang2 != 0:
    c = lang2 * 707
else:
    c = 0

ans = (a + b + c) * 4763
print(ans)