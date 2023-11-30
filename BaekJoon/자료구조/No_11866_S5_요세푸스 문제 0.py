from collections import deque
import sys
q = deque()
pop_list = list()

N, K = map(int, sys.stdin.readline().split())
for i in range(1, N+1):
    q.append(i)

while len(q) != 0:
    for j in range(K-1):
        q.append(q.popleft())
    pop_list.append(q.popleft())

print("<", end='')
for k in range(len(pop_list)-1):
    print(str(pop_list[k])+',', end=' ')
print(str(pop_list[-1])+">")
