number = list(map(int, input().split()))

print((number[0] + number[1]) % number[2])
print(((number[0] % number[2]) + (number[1] % number[2])) % number[2])
print((number[0] * number[1]) % number[2])
print(((number[0] % number[2]) * (number[1] % number[2])) % number[2])