from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
m_unit = deque()
m_unit_size = len(m_unit) - 1
r = 0
cnt = 0
for i in range(N):
    m_unit.append(int(sys.stdin.readline()))

if m_unit[int(m_unit_size / 4)] > K:
    r = m_unit_size / 4
elif m_unit[int(m_unit_size / 2)] > K:
    r = m_unit_size / 2
elif m_unit[int(m_unit_size * 0.75)] > K:
    r = int(len(m_unit) * 0.75)
else:
    r = len(m_unit) - 1


for j in range(r, -1, -1):
    cnt = cnt + (K // m_unit[j])
    K = K % m_unit[j]

print(cnt)
