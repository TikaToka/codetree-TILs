n = int(input())

nums = list(map(int, input().split()))
total = sum(nums)
dp = [False] * (total+1)
dp[0] = True

for i in range(len(nums)):
    for j in range(total, 0, -1):
        dp[j] = dp[j] or dp[j-nums[i]]
        
if total%2 != 0:
    print("No")
else:
    if dp[total//2]:
        print("Yes")
    else:
        print("No")
