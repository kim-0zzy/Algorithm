from collections import deque
import sys

cyc = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
l.sort()
q = deque(l)

for i in range(1, len(q)):
    q[i] = q[i] + q[i-1]

print(sum(q))
