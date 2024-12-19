n, m = map(int, input().split())

nums = [x for x in map(int, input().split())]

dp = [10001 for _ in range(m+1)]
dp[0] = 0

for j in range(len(nums)):
    for i in range(m, -1, -1):
            if i >= nums[j]:
                dp[i] = min(dp[i-nums[j]]+1, dp[i])



if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])

