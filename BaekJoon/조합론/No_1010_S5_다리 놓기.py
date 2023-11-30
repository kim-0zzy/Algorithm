def factorial(n):
    if n < 2:
        return 1
    else:
        answer = 1
        for x in range(1, n + 1):
            answer *= x
        return answer


cyc = int(input())
for i in range(cyc):
    a, b = map(int, input().split())
    aa = max(a, b)
    bb = min(a, b)

    print((factorial(aa) // (factorial(bb) * factorial(aa - bb))))
