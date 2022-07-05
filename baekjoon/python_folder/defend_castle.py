# https://www.acmicpc.net/problem/1236

# 1. 입력받은 경비 현황지도에서 처리 된 부분을 저장
# 2. 각 행, 열 중 남은 부분의 수가 더 큰 값이 경비 수와 같음

N, M = map(int, input().split())

castle = [list(input()) for _ in range(N)]
row_table = set()
col_table = set()
for i in range(N):
    for j in range(M):
        if castle[i][j] == 'X':
            row_table.add(i)
            col_table.add(j)

row_remain = N - len(row_table)
col_remain = M - len(col_table)
print(max(row_remain, col_remain))