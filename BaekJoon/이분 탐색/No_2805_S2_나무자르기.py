import sys


def binary_search(target, start, end):
    if start > end:
        return end
    mid = (start + end) // 2
    bi_cnt = 0
    for x in range(N):
        if height_list[x] > mid:
            bi_cnt += height_list[x] - mid

    if target == bi_cnt:
        return mid
    elif target < bi_cnt:
        return binary_search(target, mid + 1, end)
    else:
        return binary_search(target, start, mid - 1)


N, M = map(int, sys.stdin.readline().split())
height_list = list(map(int, sys.stdin.readline().split()))
longest_tree = max(height_list)
print(binary_search(M, 1, longest_tree))
