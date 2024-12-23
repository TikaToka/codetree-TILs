n = int(input())

nums = list(map(int, input().split()))

total = sum(nums)

dp = [0] * (n+1)

for i in range(len(nums)):
    for j in range(n, 0, -1):
        dp[j] = max(dp[j], dp[j-1] + nums[i]) # abs((dp[j] - nums[i]) - (dp[j-1] + nums[i])))

for i in range(1, n-1):
    dp[i] = abs(total - 2 * dp[i])

print(min(dp[1:n+1]))