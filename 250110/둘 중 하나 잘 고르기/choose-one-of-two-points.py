n = int(input())
red = []
blue = []

for _ in range(2 * n):
    r, b = map(int, input().split())
    red.append(r)
    blue.append(b)

# Write your code here!
dp = [[0 for _ in range(n+1)] for _ in range(2*n)]
dp[0][0] = blue[0]
dp[0][1] = red[0]


for i in range(1, 2*n):
    for j in range(n+1): # red 갯수
        if j == 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + blue[i])
        else:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + red[i], dp[i-1][j] + blue[i])



print(dp[2*n-1][n])
