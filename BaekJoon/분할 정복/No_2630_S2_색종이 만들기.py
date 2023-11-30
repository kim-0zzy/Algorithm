import sys
def slice_sqr(x, y, n):
    global w, b
    sqr = sqr_arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if sqr != sqr_arr[i][j]:
                slice_sqr(x, y, n // 2)
                slice_sqr(x, y + n // 2, n // 2)
                slice_sqr(x + n // 2, y, n // 2)
                slice_sqr(x + n // 2, y + n // 2, n // 2)
                return

    if sqr == 0:
        w += 1
    else:
        b += 1
    return


A = int(sys.stdin.readline())
sqr_arr = [0 for i in range(A)]

for i in range(A):
    sqr_arr[i] = list(map(int, sys.stdin.readline().strip().split()))

w, b = 0, 0
slice_sqr(0, 0, A)
print(w)
print(b)
