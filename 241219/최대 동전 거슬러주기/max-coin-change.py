n, m = map(int, input().split())

dp = [-999] * (m+1)

coin = [x for x in map(int, input().split())]

dp[0] = 0

for i in range(m+1):
    for j in range(len(coin)):
        if i >= coin[j]:
            if dp[i-coin[j]] == -999:
                continue
            dp[i] = max(dp[i], dp[i - coin[j]] + 1)


if dp[m] == -999:
    print(-1)
else:
    print(dp[m])

