import sys

n = int(sys.stdin.readline().strip())
x = sys.stdin.readline().strip()

cnt_b = x.count("B")
cnt_s = x.count("S")
cnt_a = x.count("A")

if cnt_b == cnt_s == cnt_a:
    print("SCU")
else:
    max_cnt = max(cnt_b,cnt_s,cnt_a)
    ans = []
    if cnt_b == max_cnt:
        ans.append("B")
    if cnt_s == max_cnt:
        ans.append("S")
    if cnt_a == max_cnt:
        ans.append("A")
    print("".join(ans))
    
