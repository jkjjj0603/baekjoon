import sys


for line in sys.stdin:
    i = 0
    s,t = line.split()
    for j in range(len(t)):
        if t[j] == s[i]:
            i+=1
        if i == len(s):
            break
    if i == len(s):
        print("Yes")
    else:
        print("No")        