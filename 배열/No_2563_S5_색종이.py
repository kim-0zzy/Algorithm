sqr_scatch = [[0 for i in range(100)]for i in range(100)]
n = int(input())
a_min = 99999
b_max = 0
cnt = 0
while(n  != 0):
    a,b = map(int, input().split())
    a_min = min(a_min,a)
    b_max = max(b_max,b)
    for i in range(a, a+10):
        for j in range(b, b+10):
            if sqr_scatch[i][j] == 0:
                sqr_scatch[i][j] = 1
                cnt +=1
    n -= 1
print(cnt)

