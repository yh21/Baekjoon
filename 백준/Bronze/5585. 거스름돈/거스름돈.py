coin = [500, 100, 50, 10, 5, 1]
money = 1000 - int(input())
count = 0

for each_coin in coin:
    if money >= each_coin:
        count += money // each_coin
        money %= each_coin  

print(count)