n = int(input())

board = [[x for x in map(int, input().split())] for _ in range(n)]

dp = [[99999999999999999999999 for _ in range(n)] for _ in range(n)]

dp[0][n-1] = board[0][n-1]

for i in range(1, n):
    dp[i][n-1] = dp[i-1][n-1] + board[i][n-1]

for i in range(n-2, -1, -1):
    dp[0][i] = dp[0][i+1] + board[0][i]


for i in range(1, n):
    for j in range(n-2, -1, -1):
        dp[i][j] = min(dp[i-1][j] + board[i][j], dp[i][j+1] + board[i][j])


    
print(dp[n-1][0])