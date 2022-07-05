# https://www.acmicpc.net/problem/1292

# (1 2 2 3 3 3 4 4 4 4 ...) 와 같은 수열이므로
# 1 2 3 4 5 6 find_fraction.py 와 비슷한 규칙같아 보이긴 하지만
# 때로는 간단한 방법이 더 빠른 풀이가 되기도 함

A, B = map(int, input().split())

arr = [0]
for i in range(1, B+1):
    for j in range(i):
        arr.append(i)

total = 0
for i in range(A, B+1):
    total += arr[i]

print(total)