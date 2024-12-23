import sys

n = int(input())

nums = list(map(int, input().split()))

total = sum(nums)

dp = [0] * (n+1)
dp2 = [0] * (n+1)
for i in range(len(nums)):
    for j in range(n-1, 0, -1):
        dp[j] = max(dp[j], dp[j-1] + nums[i]) # abs((dp[j] - nums[i]) - (dp[j-1] + nums[i])))
        dp2[j] = total - dp[j]

answer = sys.maxsize

for i in range(1, n):
    answer = min(abs(dp[i] - dp2[i]), answer)

print(answer)