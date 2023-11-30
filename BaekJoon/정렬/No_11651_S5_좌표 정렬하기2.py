import sys

cyc = int(sys.stdin.readline())
x_arr = list()
y_arr = list()
arr = list()
for i in range(0, cyc):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([y, x])

arr = sorted(arr)
for i in range(0, cyc):
    print(arr[i][1], arr[i][0])
