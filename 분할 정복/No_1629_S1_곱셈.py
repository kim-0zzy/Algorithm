import sys


def mulitply(a, b, c):
    if b == 1:
        return a % c
    A = mulitply(a, b // 2, c)
    if b % 2 == 0:
        return (A * A) % c
    else:
        return (A * A * a) % c


a, b, c = map(int, sys.stdin.readline().split())
print(mulitply(a, b, c))
