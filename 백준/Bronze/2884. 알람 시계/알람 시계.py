time = list(map(int, input().split()))
total = (1395 + time[0] * 60 + time[1]) % 1440

print(total // 60, total % 60)