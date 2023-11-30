import sys

A = list()
func_list = list()
cyc = int(sys.stdin.readline())
cnt = 0
for i in range(cyc):
    func_list = sys.stdin.readline().strip().split()
    if func_list[0] == 'push':
        A.append(func_list[1])

    elif func_list[0] == 'pop':

        if (len(A) - cnt) >= 1:
            print(A[cnt])
            cnt += 1
        else:
            print(-1)

    elif func_list[0] == 'size':
        print(len(A) - cnt)

    elif func_list[0] == 'empty':
        if (len(A) - cnt) >= 1:
            print(0)
        else:
            print(1)

    elif func_list[0] == 'front':
        if (len(A) - cnt) < 1:
            print(-1)
        else:
            print(A[cnt])

    elif func_list[0] == 'back':
        if (len(A) - cnt) < 1:
            print(-1)
        else:
            print(A[-1])
