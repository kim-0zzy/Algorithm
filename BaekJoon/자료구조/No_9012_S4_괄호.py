import sys

cyc = int(sys.stdin.readline())

for i in range(cyc):
    stack = 0
    a = list(input())
    for LR in a:
        if LR == '(':
            stack += 1
        elif LR == ')':
            stack -= 1

        if stack < 0:
            break

    if stack == 0:
        print("YES")
    else:
        print('NO')
