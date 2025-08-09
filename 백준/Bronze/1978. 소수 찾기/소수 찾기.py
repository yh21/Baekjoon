n = int(input())
numbers = list(map(int, input().split()))
total = 0

for i in range(0, n):
    for j in range(2, numbers[i]):
        if (numbers[i] % j) == 0:
            total += 1
            break
if 1 in numbers:
    total += 1

print(len(numbers) - total)