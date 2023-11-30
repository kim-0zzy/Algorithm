import sys

def binary_search(target, start, end):
    if start > end:
        return end
    mid = (start + end) // 2
    bi_cnt = 0
    for x in range(len(lan_list)):
        bi_cnt += lan_list[x] // mid

    if target <= bi_cnt:
        return binary_search(target, mid + 1, end)
    else:
        return binary_search(target, start, mid - 1)


N, K = map(int, sys.stdin.readline().split())
lan_list = list()
for i in range(N):
    lan_list.append(int(sys.stdin.readline()))

longest_lan_cable = max(lan_list)

print(binary_search(K, 1, longest_lan_cable))
