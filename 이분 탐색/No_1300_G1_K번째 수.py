import sys


def binary_search(start, end):
    if start > end:
        return start
    mid = (start + end) // 2
    bi_cnt = 0
    for x in range(1, N+1):
        bi_cnt += min(mid // x, N)

    if k <= bi_cnt:
        return binary_search(start, mid - 1)
    else:
        return binary_search(mid + 1, end)



N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

if N**2 == k:
    print(k)
else:
    print(binary_search(1, N**2))
