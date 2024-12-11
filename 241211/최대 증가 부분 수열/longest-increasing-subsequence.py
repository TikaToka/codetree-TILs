n = int(input())
board = [x for x in map(int, input().split())]

dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(0, i):
        if board[j] < board[i]:
            dp[i] = max(dp[i], dp[j]+1)


print(max(dp))