import collections
import sys

cyc = int(sys.stdin.readline())
num_arr = [0] * cyc

avg = 0
mid = 0
most = 0
scope = 0

for i in range(0, cyc):
    num_arr[i] = int(sys.stdin.readline())

num_arr.sort()
avg = round(sum(num_arr) / cyc)
mid = num_arr[cyc // 2]
scope = max(num_arr) - min(num_arr)
most = collections.Counter(num_arr).most_common(2)

if cyc > 1:
    if most[0][1] == most[1][1]:
        most = max(most[0][0], most[1][0])
    else:
        most = most[0][0]
else:
    most = num_arr[0]

print("{}\n{}\n{}\n{}".format(avg, mid, most, scope))
