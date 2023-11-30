import sys


def dynamic_fibo(n):
    if n == 1:
        return 1
    else:
        for i in range(3, n+1):
            n_list[i] = (n_list[i-1] + n_list[i-2]) % 15746
    return n_list[n]


n = int(sys.stdin.readline())
n_list = [0 for i in range(n+1)]
if n > 1:
    n_list[1] = 1
    n_list[2] = 2
else:
    n_list[1] = 1
print(dynamic_fibo(n))
