num = list(input())
num = list(map(int, num))
num.sort(reverse=True)
for i in range(0, len(num)):
    print(num[i], end="")
