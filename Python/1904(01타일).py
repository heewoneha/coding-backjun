dp = [1, 2, 3]

N = int(input())

for i in range(3, N):
    dp.append((dp[i-1] + dp[i-2]) % 15746)

print(dp[N-1])