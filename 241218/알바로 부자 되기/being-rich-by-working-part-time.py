n = int(input())

board = [[x for x in map(int, input().split())] for _ in range(n)]

dp = [x[2] for x in board]


# board.sort(key=lambda x: x[1])


answer = 0

for i in range(1, n):
    for j in range(i):
        if board[j][1] < board[i][0]:
            dp[i] = max(dp[i], dp[j] + board[i][2])

print(max(dp))