now = list(map(int, input().split()))
time = int(input())
result = (now[0] * 60 + now[1] + time) % 1440

print(result // 60, result % 60)