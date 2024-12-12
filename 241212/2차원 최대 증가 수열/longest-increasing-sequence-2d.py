n, m = map(int, input().split())

board = [[x for x in map(int, input().split())] for _ in range(n)]

dp = [[1 for _ in range(m)] for _ in range(n)]


for i in range(0, n):
    for j in range(0, m):
        for a in range(0, i):
            for b in range(0, j):
                if board[i][j] > board[a][b]:
                    dp[i][j] = max(dp[i][j], dp[a][b] + 1)

answer = 0
for i in range(n):
    for j in range(m):
        answer = max(answer, dp[i][j])

print(answer)