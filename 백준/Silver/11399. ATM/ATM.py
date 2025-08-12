n = int(input())
people = list(map(int, input().split()))
people.sort()
total = 0

for i in range(0, n):
    total = total + people[i] * (n - i)

print(total)