n = int(input())

board = [x for x in map(int, input().split())]
dp = [-1] * n
dp[0] = 0

for i in range(1, n):
    for j in range(0, i):
        if dp[j] == -1:
            continue
        if board[j] + j >= i:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))