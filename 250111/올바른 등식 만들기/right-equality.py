N, M = map(int, input().split())
nums = list(map(int, input().split()))

# Write your code here!
cand = []
cand.append(nums[0])
cand.append(-1 * nums[0])
for i in range(1, N):
    temp = []
    for j in cand:
        c = j + nums[i]
        if c <= 20:
            temp.append(j + nums[i])
        c = j - nums[i]
        if c >= -1 * 20:
            temp.append(j - nums[i])
    cand = temp

answer = 0

for i in cand:
    if i == M:
        answer += 1

print(answer)