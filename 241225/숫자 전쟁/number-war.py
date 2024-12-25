n = int(input().strip())

# a, b를 1~n 인덱스로 쓰기 위해 앞에 dummy 0 하나씩
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))

# dp[i][j] = 플레이어1이 i장 소모, 플레이어2(남우)가 j장 소모한 상태에서
# 남우가 앞으로 얻을 수 있는 최대 점수
dp = [[0]*(n+1) for _ in range(n+1)]

# 뒤에서부터 채움: i, j를 n부터 0까지 내려오면서 계산
# (i, j) 상태에서 다음 카드가 a[i+1], b[j+1]라고 생각
for i in range(n, -1, -1):
    for j in range(n, -1, -1):
        # 이미 한쪽이 n장을 소모(즉 카드가 0장 남음)한 상태면 dp[i][j] = 0
        # => 코드상 초기값이 0이므로 그냥 넘어감
        if i == n or j == n:
            dp[i][j] = 0
            continue

        # 1) 둘 다 버리기(discard)
        discard = dp[i+1][j+1]

        # 2) 카드 대결(battle)
        if a[i+1] < b[j+1]:
            # 상대 카드(a[i+1])만 소모
            battle = dp[i+1][j]
        elif a[i+1] > b[j+1]:
            # 남우 카드(b[j+1])만 소모 + 남우 점수 증가
            battle = dp[i][j+1] + b[j+1]
        else:  # a[i+1] == b[j+1] (동점 -> 둘 다 버림, 점수 없음)
            battle = dp[i+1][j+1]

        dp[i][j] = max(discard, battle)

# 결과를 계산하여 출력합니다.
ans = 0
for i in range(n + 1):
    ans = max(ans, dp[i][0])
    ans = max(ans, dp[0][i])

print(ans)