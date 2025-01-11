N, M = map(int, input().split())
nums = list(map(int, input().split()))

OFFSET = 20
dp = [0] * (2 * OFFSET + 1)  # 가능한 값 범위 [-20, 20]을 저장

# 첫 번째 숫자를 초기화
dp[nums[0] + OFFSET] += 1
dp[-nums[0] + OFFSET] += 1

# 각 단계별로 가능한 상태만 업데이트
for i in range(1, N):
    next_dp = [0] * (2 * OFFSET + 1)  # 현재 단계의 유효한 상태만 추적
    for x in range(-OFFSET, OFFSET + 1):
        if dp[x + OFFSET] > 0:  # 이전 단계에서 유효했던 상태만 사용
            # 숫자를 더하거나 뺀 경우
            if x + nums[i] <= OFFSET:
                next_dp[x + nums[i] + OFFSET] += dp[x + OFFSET]
            if x - nums[i] >= -OFFSET:
                next_dp[x - nums[i] + OFFSET] += dp[x + OFFSET]
    dp = next_dp  # 현재 단계의 상태를 갱신

# 최종 결과 출력
print(dp[M + OFFSET])
