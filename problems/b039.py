import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):

    line = sys.stdin.readline().strip()
    while line == "":
        line = sys.stdin.readline().strip()

    n,m = map(int,line.split())

    n_power = []
    while len(n_power) < n:
        n_power += list(map(int,sys.stdin.readline().split()))

    m_power = []
    while len(m_power) < m:
        m_power += list(map(int,sys.stdin.readline().split()))

    n_power.sort()
    m_power.sort()

    i = 0
    j = 0
    while i < n and j < m:
        if n_power[i] < m_power[j]:
            i += 1
        else:
            j += 1

    if i == n:
        print("B")
    elif j == m:
        print("S")
    else:
        print("C")