n = int(input())
length = list(map(int, input().split()))
cost = list(map(int, input().split()))
total = 0
now_price = cost[0]

for i in range(0, n - 1):
    total += now_price * length[i]

    if cost[i + 1] < now_price:
        now_price = cost[i + 1]

print(total)