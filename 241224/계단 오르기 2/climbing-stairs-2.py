n = int(input())

coins = [0]
coins += list(map(int, input().split()))

dp = [[0 for _ in range(4)] for _ in range(n+1)]

# for i in range(0, n+1):
#     for j in range(i):
#         dp[i][0] += coins[j]

# print(dp)
for j in range(1, 4):
    for i in range(1, n+1):
        dp[i][j] = max(dp[i][j], dp[i-2][j] + coins[i], dp[i-1][j-1] + coins[i]) # 2
        

maxval = 0
for i in range(4):
    maxval = max(maxval, dp[n][i])
print(maxval)