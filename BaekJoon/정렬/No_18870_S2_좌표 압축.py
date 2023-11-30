import sys

cyc = int(sys.stdin.readline())
point = list(sys.stdin.readline().split())
point = list(map(int, point))

set_point = list(set(point))
set_point.sort()
point_dict = {}

for i in range(len(set_point)):
    point_dict[set_point[i]] = i

for j in point:
    print(point_dict[j], end=' ')
