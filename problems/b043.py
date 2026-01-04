import sys

n = int(sys.stdin.readline().strip())
classes = []
best_cnt = -1
best_student = 1

for _ in range(n):
    classes.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    cnt = 0
    for j in range(n):
        if i == j:
            continue
        for k in range(5):
            if classes[i][k] == classes[j][k]:
                cnt += 1
                break
            
    student_num = i + 1
    if cnt > best_cnt:
        best_cnt = cnt
        best_student = student_num
    elif cnt == best_cnt or student_num < best_student:
        best_student = student_num

print(best_student)
         