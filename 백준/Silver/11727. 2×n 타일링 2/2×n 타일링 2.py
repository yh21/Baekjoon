N = int(input())

dp = list()
for _ in range(N + 1):
    dp.append(0)

dp[0] = 1
dp[1] = 3

for i in range(2, N + 1):
    dp[i] = (dp[i - 1]) % 10007 + (2 * dp[i - 2]) % 10007

print(dp[N - 1] % 10007)