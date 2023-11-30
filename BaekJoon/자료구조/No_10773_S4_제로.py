import sys

cyc = int(sys.stdin.readline())
a_list = list()

for i in range(cyc):
    num = int(sys.stdin.readline())
    if num != 0:
        a_list.append(num)
    else:
        del a_list[-1]

print(sum(a_list))
