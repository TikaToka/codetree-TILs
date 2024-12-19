n, m = map(int, input().split())

coins = list(map(int, input().split()))

dp = [100001] * (m+1)
dp[0] = 0

for i in range(len(coins)):
    for j in range(m, -1, -1):
        if j >= coins[i]:
            if dp[j-coins[i]] == 100001:
                continue
            dp[j] = min(dp[j-coins[i]]+1,  dp[j])

if dp[m] != 100001:
    print("Yes")
else:
    print("No")
