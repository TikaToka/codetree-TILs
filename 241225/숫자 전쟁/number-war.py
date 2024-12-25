n = int(input())

a = [0]
a += list(map(int, input().split()))
b = [0]
b += list(map(int, input().split()))

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]



for i in range(1, n+1):
    for j in range(1, n+1):
        if a[i] <= b[j]:
            # if dp[i-1][j-1] != 0:
            dp[i][j] = max(dp[i-1][j-1], dp[i][j])
            # if dp[i-1][j] != 0:
            dp[i][j] = max(dp[i-1][j], dp[i][j])
        else:
            # if dp[i][j-1] != 0:
            dp[i][j] = max(dp[i][j], dp[i][j-1] + b[j])
        
print(dp[n][n])