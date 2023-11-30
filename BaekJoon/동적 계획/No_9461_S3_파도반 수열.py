import sys


def dynamic_fibo(n):
    if n <= 10:
        return wave_sequence[n]
    else:
        for i in range(11, n+1):
            wave_sequence[i] = wave_sequence[i-1] + wave_sequence[i-5]
        return wave_sequence[n]


wave_sequence = [0 for i in range(101)]
wave_sequence[3], wave_sequence[1], wave_sequence[2] = 1, 1, 1
wave_sequence[4], wave_sequence [5] = 2, 2
wave_sequence[6] = 3
wave_sequence[7] = 4
wave_sequence[8] = 5
wave_sequence[9] = 7
wave_sequence[10] = 9

t = int(sys.stdin.readline())
while t != 0:
    n = int(sys.stdin.readline())
    print(dynamic_fibo(n))
    t -= 1
