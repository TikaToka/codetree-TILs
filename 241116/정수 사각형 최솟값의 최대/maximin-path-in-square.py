n = int(input())

board = [[x for x in map(int, input().split())] for _ in range(n)]

dp = [[10000000 for _ in range(n)] for _ in range(n)]

dp[0][0] = board[0][0]
for i in range(1, n):
    dp[i][0] = min(board[i][0], dp[i-1][0])
    dp[0][i] = min(board[0][i], dp[0][i-1])

for i in range(1, n-1):
    for j in range(1, n-1):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1], board[i][j])

if dp[n-1][n-1] >= board[n-1][n-1]:
    print(board[n-1][n-1])
elif dp[n-1][n-1] < board[n-1][n-1]:
    print(max(dp[n-2][n-1], dp[n-1][n-2]))
