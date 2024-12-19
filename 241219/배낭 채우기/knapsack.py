n, m = map(int, input().split())

diamonds = [list(map(int, input().split())) for _ in range(n)]

dp = [-1] * (m+1)
dp[0] = 0


for i in diamonds:
    for j in range(m, -1, -1):
        if j >= i[0]:
            if dp[j - i[0]] == -1:
                continue
            dp[j] = max(dp[j], dp[j-i[0]] + i[1])

print(max(dp))