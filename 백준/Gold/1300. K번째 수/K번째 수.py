n = int(input())
k = int(input())

low, high = 1, n * n
while low < high:
    mid = (low + high) // 2
    count = sum(min(mid // i, n) for i in range(1, n + 1))
    if count < k:
        low = mid + 1
    else:
        high = mid
print(low)