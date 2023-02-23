T = int(input())

for _ in range(0, T):
    dp = [1, 2, 4]

    N = int(input())

    for i in range(3, N):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    
    print(dp[N-1])