N, M = map(int, input().split())
nums = list(map(int, input().split()))

# Write your code here!
dp = [[-99 for _ in range(2**(N-1))] for _ in range(N)]
dp[0][0] = nums[0]

for i in range(1, N):
    for j in range(2**(N-1)):
        if dp[i-1][j//2] != -99:
            if j % 2 == 0:
                temp = dp[i-1][j//2] + nums[i]
                if temp <= 20:
                    dp[i][j] = temp
            else:
                temp = dp[i-1][j//2] - nums[i]
                if temp >= -20:
                    dp[i][j] = temp

answer = 0
for i in range(2**(N-1)):
    if dp[N-1][i] == M:
        answer += 1

print(answer)