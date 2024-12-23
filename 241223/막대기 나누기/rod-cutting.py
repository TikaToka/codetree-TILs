n = int(input())
bars = [0]
bars += list(map(int, input().split()))
dp = [0] * (n+1)


for i in range(n+1):
    for j in range(1, 5):
        if i>=j:
            dp[i] = max(dp[i-j] + bars[j], dp[i])
print(dp[n])