n = int(input())

dp = [1 for _ in range(n)]


board = []

for i in range(n):
    a, b = map(int, input().split())
    board.append((a, b))


board.sort(key=lambda x: x[1])


for i in range(1, n):
    for j in range(0, i):
        if board[j][1] < board[i][0]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

