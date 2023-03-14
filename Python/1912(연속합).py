N = int(input())
x = list(map(int, input().split()))
dp = [0] * N

dp[0] = x[0]
for i in range(1, N):
    dp[i] = max(dp[i-1]+x[i], x[i])

print(max(dp))