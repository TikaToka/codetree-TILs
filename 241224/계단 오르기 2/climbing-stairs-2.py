n = int(input())

coins = [0]
coins += list(map(int, input().split()))

dp = [[0 for _ in range(4)] for _ in range(n+1)]

dp[1][1] = 1

for j in range(0, 4):   
    for i in range(2, n+1):
        if j >= 1:
            dp[i][j] = max(dp[i][j], dp[i-2][j] + coins[i], dp[i-1][j-1] + coins[i]) # 2
        else:
            dp[i][j] = max(dp[i][j], dp[i-2][j] + coins[i])
print(dp)
        

maxval = 0
for i in range(4):
    maxval = max(maxval, dp[n][i])
print(maxval)

# 0
# 0 2 0 6
# 1
# 2
# 3
