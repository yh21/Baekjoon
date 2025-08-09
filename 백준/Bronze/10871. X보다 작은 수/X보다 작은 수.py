stan = list(map(int, input().split()))
n = stan[0]
x = stan[1]
target = list()

numbers = list(map(int, input().split()))
for i in range(0, n):
    if numbers[i] < x:
        target.append(numbers[i])

print(*target)