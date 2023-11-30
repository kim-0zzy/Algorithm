import sys
cyc = int(input())
arr = list()

for i in range(0, cyc):
    a = int(sys.stdin.readline())
    arr.append(a)
arr.sort()

for i in range(0,cyc):
    print(arr[i])
