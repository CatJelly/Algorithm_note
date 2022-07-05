# https://www.acmicpc.net/problem/1110

# 패턴 대로 처리
# ex)
# N = 26
# 2 + 6 = 8 -> N = 68 cnt = 1
# 6 + 8 = 14 -> N = 84 cnt = 2 
# 8 + 4 = 12 -> N = 42 cnt = 3
# 4 + 2 = 6 -> N = 26 cnt = 4
# cycle = 4

N = int(input())
n = N
cycle = 0
res = -1

while res != N:
    # temp = int(n / 10) + n % 10
    temp = n // 10 + n % 10
    res = n % 10 * 10 + temp % 10
    n = res
    cycle +=1 

print(cycle)
