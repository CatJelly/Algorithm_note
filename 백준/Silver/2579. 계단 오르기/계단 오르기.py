# 계단 오르기
# 아래 시작점부터 꼭대기까지 가는 겜
# 계단을 밟으면 써있는 점수 획득
# 계단 오르는 규칙
# 1. 계단은 한번에 한계단, 두계단씩 오를수 있음
# 2. 연속된 세 계단 모두 밟기 X (시작점 미포함)
# 3. 마지막 도착 계단은 반드시 밟음

n = int(input())

scores = [int(input()) for _ in range(n)]

dp = [0 for _ in range(n)]
if n <= 2:
    print(sum(scores))
else:
    dp[0] = scores[0]
    dp[1] = scores[0] + scores[1]
    for i in range(2, n):
        dp[i] = max(dp[i-3] + scores[i-1] + scores[i], dp[i-2] + scores[i])

    print(dp[-1])
