n = int(input())

a = [0]
a += list(map(int, input().split()))
b = [0]
b += list(map(int, input().split()))

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]


for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        # battle
        if a[i+1] < b[j+1]:
            battle = dp[i+1][j]
        elif a[i+1]>b[j+1]:
            battle = dp[i][j+1] + b[j+1]
        else:
            battle = dp[i+1][j+1]
        # discatd
        dp[i][j] = max(dp[i+1][j+1], battle)

answer = 0

for i in range(1, n+1):
    answer = max(answer, max(dp[i]))

print(answer)