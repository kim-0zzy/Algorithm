import sys


def binary_search(target, start, end):
    if start > end:
        return end
    mid = (start + end) // 2
    bi_cnt = 1
    install_point = distance_list[0]
    for x in range(1, N):
        if distance_list[x] - install_point >= mid:
            bi_cnt += 1
            install_point = distance_list[x]

    if target <= bi_cnt:
        return binary_search(target, mid + 1, end)
    else:
        return binary_search(target, start, mid - 1)


N, C = map(int, sys.stdin.readline().split())
distance_list = [0 for i in range(N)]
for i in range(N):
    distance_list[i] = int(sys.stdin.readline().strip())
distance_list = sorted(distance_list)

print(binary_search(C, 1, distance_list[-1] - distance_list[0]))
