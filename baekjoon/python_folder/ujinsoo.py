# https://www.acmicpc.net/problem/1356


N = list(map(int, input()))

ans = "NO"

for i in range(1, len(N)):
    res1, res2 = 1, 1
    for j in range(i):
        res1 *= N[j]
    
    for j in range(i, len(N)):
        res2 *= N[j]

    if res1 == res2:
        ans = "YES"

print(ans)