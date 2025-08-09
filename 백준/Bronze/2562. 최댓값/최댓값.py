numbers = list()
for i in range(0, 9):
    numbers.append(int(input()))

max = max(numbers)
print(max)

for i in range(0, 9):
    if numbers[i] == max:
        print(i + 1)
        break
