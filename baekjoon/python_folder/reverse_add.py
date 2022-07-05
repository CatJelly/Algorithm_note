# https://www.acmicpc.net/problem/1357

def Rev(X):
    X = str(X)
    res = ""
    for i in range(len(X) - 1, -1, -1):
        res += X[i]
    return int(res)

X, Y = map(int, input().split())

print(Rev(Rev(X) + Rev(Y)))