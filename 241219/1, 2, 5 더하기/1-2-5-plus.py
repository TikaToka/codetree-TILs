board = [1, 2, 5]

n = int(input())

dp = [0] * (n+1)
 
dp[0] = 1 # 0을 만드는 방법 1가지 


for i in range(n+1):
    for j in range(len(board)):
        if i >= board[j]:
            dp[i] = dp[i] + dp[i-board[j]]

print(dp[n] % 10007)
