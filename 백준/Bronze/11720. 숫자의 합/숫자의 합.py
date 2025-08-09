n = int(input())
numbers = list(map(int, input()))
total = 0

for i in range(0, n):
        total += numbers[i]

print(total)