import sys

cyc = int(sys.stdin.readline())
time = list()

for i in range(cyc):
    start_time, end_time = map(int, input().split())
    time.append([start_time, end_time])

time = sorted(time, key=lambda a: a[0])
time = sorted(time, key=lambda a: a[1])

last = 0
cnt = 0

for j, k in time:
    if j >= last:
        cnt += 1
        last = k

print(cnt)
