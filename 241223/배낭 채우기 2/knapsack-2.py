n, m = map(int, input().split())

dp = [0] * (m+1)

dias = []

for i in range(n):
    dias.append((list(map(int, input().split()))))

for i in range(1, m+1):
    for j in range(len(dias)):
        if i >= dias[j][0]:
            dp[i] = max(dp[i-dias[j][0]]+dias[j][1], dp[i])

print(dp[m])