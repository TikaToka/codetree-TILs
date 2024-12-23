import sys

n = int(input())

nums = list(map(int, input().split()))

total = sum(nums)

dp = [False] * (total+1)
dp[total] = True
dp[0] = True
for i in range(len(nums)):
    for j in range(total, 0, -1):
        dp[j] = dp[j] or dp[j-nums[i]]

for i in range(len(dp)//2, 0, -1):
    if dp[i]:
        print(abs(total-2*i))
        break
