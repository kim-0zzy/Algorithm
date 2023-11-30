import sys

city_range = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
oil_price = list(map(int, sys.stdin.readline().split()))
total_price = list()
cheap_price = oil_price[0]
total_price.append(distance[0] * cheap_price)

for i in range(1, city_range - 1):
    if cheap_price > oil_price[i]:
        cheap_price = oil_price[i]
    total_price.append(distance[i] * cheap_price)

print(sum(total_price))
