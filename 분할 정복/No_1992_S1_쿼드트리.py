import sys
def slice_sqr(x, y, n):
    global word
    sqr = sqr_arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if sqr != sqr_arr[i][j]:
                word += '('
                slice_sqr(x, y, n // 2)
                slice_sqr(x, y + n // 2, n // 2)
                slice_sqr(x + n // 2, y, n // 2)
                slice_sqr(x + n // 2, y + n // 2, n // 2)
                word += ')'
                return

    if sqr == 0:
        word += '0'
    else:
        word += '1'
    return


A = int(sys.stdin.readline())
sqr_arr = [0 for i in range(A)]

for i in range(A):
    sqr_arr[i] = list(map(int, sys.stdin.readline().strip()))
word = ''
slice_sqr(0, 0, A)
print(word)
