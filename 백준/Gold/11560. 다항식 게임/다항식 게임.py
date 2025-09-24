import sys

nums = int(input())
bucket = list()
for i in range(0, nums):
    k, N = map(int, (sys.stdin.readline().strip().split()))
    dp = [[0] * (211) for _ in range(k + 1)]
    dp[0][0] = 1

    for i in range(1, k + 1):
        for j in range(0, 211):
            for t in range(0, i + 1):
                if j - t >= 0:
                    dp[i][j] += dp[i - 1][j - t]
    bucket.append(dp[k][N])

for i in range(nums):
    print(bucket[i])