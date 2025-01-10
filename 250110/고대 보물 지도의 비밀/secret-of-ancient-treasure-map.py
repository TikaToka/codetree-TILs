n, k = map(int, input().split())
numbers = list(map(int, input().split()))

# Write your code here!
dp = [[0 for _ in range(k+1)] for _ in range(n)]
dp[0][0] = numbers[0]

for i in range(1, n):
    for j in range(0, k+1):
        if numbers[i] >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j]+numbers[i])
        elif numbers[i] < 0:
            if j == 0:
                dp[i][j+1] = max(dp[i][j+1], dp[i-1][j] + numbers[i], numbers[i])
            elif dp[i-1][j-1] != 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1]+numbers[i])
answer = 0
for i in range(n):
    for j in range(k+1):
        if dp[i][j] > answer:
            answer = dp[i][j]

print(answer)