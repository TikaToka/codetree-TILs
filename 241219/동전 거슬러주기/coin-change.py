n, m = map(int, input().split())

coin = [x for x in map(int, input().split())]


dp = [99999999 for _ in range(m+1)]
dp[0] = 0

for i in range(1, m+1):
    for j in range(n):
        if i >= coin[j]:
            dp[i] = min(dp[i], dp[i-coin[j]] + 1)


if dp[m] == 99999999:
    print(-1)
else:
    print(dp[m])