import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    balance = 0
    s = sys.stdin.readline().strip()
    for ch in s:
        
        if ch == "(":
            balance += 1
        elif ch == ")":
            balance -= 1
        
        if balance < 0:
            print("NO")
            break
    else:
        if balance == 0:
          print("YES")
        else:
            print("NO")