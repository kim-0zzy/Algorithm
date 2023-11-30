import math
limit_a,limit_b = map(int, input().split())
state=0
for i in range(limit_a, limit_b+1):
    if i < 2:
        continue
    for j in range(2, int(math.sqrt(i) +1) ):
        if i % j == 0:
            state = 1
            break

    if state == 1:
        state = 0
        continue
    else:
        print(i)
