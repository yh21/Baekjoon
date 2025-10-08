import sys

N, K = map(int, sys.stdin.readline().strip().split())
weight = list()
value = list()

for _ in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    weight.append(a)
    value.append(b)

dp = [([0] * (K + 1)) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(K + 1):
        if weight[i - 1] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i - 1]] + value[i - 1])

print(dp[N][K])