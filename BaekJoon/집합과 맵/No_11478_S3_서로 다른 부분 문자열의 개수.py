import sys

A = list(sys.stdin.readline().strip())
A_dict = {}
weighted = 2
state = 0
cnt = 0
for i in range(len(A)):
    if A[i] not in A_dict:
        A_dict[A[i]] = 0
        cnt += 1
while state != 1:
    for j in range(len(A)):
        if j+weighted > len(A):
            if weighted >= len(A):
                state = 1
            break
        if ''.join(A[j:j+weighted]) not in A_dict:
            A_dict[''.join(A[j:j+weighted])] = 0
            cnt += 1
    weighted += 1

print(cnt)
