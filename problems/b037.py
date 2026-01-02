import sys

yeondu = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())

best_name = ""
best_score = -1

for _ in range(n):
    team = sys.stdin.readline().strip()
    s = yeondu + team

    l_cnt = s.count("L")
    o_cnt = s.count("O")
    v_cnt = s.count("V")
    e_cnt = s.count("E")

    score = (l_cnt+o_cnt) * (l_cnt+e_cnt) * (o_cnt+v_cnt) * (o_cnt+e_cnt) * (v_cnt+e_cnt) * (l_cnt+v_cnt)
    score = score % 100

    if best_score < score:
        best_score = score
        best_name = team
    
    elif score == best_score:
        if team < best_name:
            best_name = team

print(best_name)