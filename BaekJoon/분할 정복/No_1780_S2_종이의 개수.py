import sys

def slice_sqr(x, y, n):
    global num_0, num_1, n_num_1
    sqr = sqr_arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if sqr != sqr_arr[i][j]:
                slice_sqr(x, y, n // 3)
                slice_sqr(x, y + n // 3, n // 3)
                slice_sqr(x, y + (n // 3) * 2, n // 3)

                slice_sqr(x + n // 3, y, n // 3)
                slice_sqr(x + n // 3, y + n // 3, n // 3)
                slice_sqr(x + n // 3, y + (n // 3) * 2, n // 3)

                slice_sqr(x + (n // 3) * 2, y, n // 3)
                slice_sqr(x + (n // 3) * 2, y + n // 3, n // 3)
                slice_sqr(x + (n // 3) * 2, y + (n // 3) * 2, n // 3)
                return

    if sqr == 0:
        num_0 += 1
    elif sqr == 1:
        num_1 += 1
    else:
        n_num_1 += 1
    return


A = int(sys.stdin.readline())
sqr_arr = [0 for i in range(A)]

for i in range(A):
    sqr_arr[i] = list(map(int, sys.stdin.readline().strip().split()))

num_0 = 0
num_1 = 0
n_num_1 = 0
slice_sqr(0, 0, A)

print(n_num_1)
print(num_0)
print(num_1)
