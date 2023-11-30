import sys

cnt = 0
grade_sum = 0
for i in range(20):
    A = sys.stdin.readline().strip().split()
    if A[-1] == 'P':
        continue

    if A[-1] == 'A+':
        grade = 4.5
    elif A[-1] == 'A0':
        grade = 4
    elif A[-1] == 'B+':
        grade = 3.5
    elif A[-1] == 'B0':
        grade = 3.0
    elif A[-1] == 'C+':
        grade = 2.5
    elif A[-1] == 'C0':
        grade = 2.0
    elif A[-1] == 'D+':
        grade = 1.5
    elif A[-1] == 'D0':
        grade = 1.0
    elif A[-1] == 'F':
        grade = 0
    cnt += float(A[1])
    grade_sum += float(A[1]) * grade

print(grade_sum / cnt)
