import sys

while True:
    n = int(sys.stdin.readline().strip())
    if n == -1:
        break
    divs = []
    for d in range(1,n):
        if n % d == 0:
            divs.append(d)
    if sum(divs) == n:
        print(f"{n} = "+" + ".join(map(str,divs)))
    else:
        print(f"{n} is NOT perfect")
