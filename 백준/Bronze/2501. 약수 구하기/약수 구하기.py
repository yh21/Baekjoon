num = list(map(int, input().split()))
n = num[0]
k = num[1]
divisor = list()

for i in range(1, n + 1):
    if n % i == 0:
        divisor.append(i)

len = len(divisor)

if k > len:
    print('0')
else:
    print(divisor[k - 1])