import sys

while True:
    line = sys.stdin.readline().rstrip()
    ch = line[0]
    s = line[2:]
    if ch == "#":
        break
    cnt = s.lower().count(ch.lower())
    print(f"{ch} {cnt}")
    
    