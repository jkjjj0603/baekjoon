import sys

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
rec_lst = list(map(int, sys.stdin.readline().split()))

frame = {}  

for i in range(k):
    student = rec_lst[i]

    
    if student in frame:
        frame[student][0] += 1
        continue

  
    if len(frame) < n:
        frame[student] = [1, i]
    else:
      
        min_cnt = float("inf")
        for cand, info in frame.items():
            if info[0] < min_cnt:
                min_cnt = info[0]

     
        min_time = float("inf")
        remove_id = -1
        for cand, info in frame.items():
            if info[0] == min_cnt and info[1] < min_time:
                min_time = info[1]
                remove_id = cand

        
        del frame[remove_id]
        frame[student] = [1, i]


ans = sorted(frame.keys())
print(*ans)
