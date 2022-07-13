# 셀프 넘버
# d(n) = n + n각 자리수

def d(N):
    total = N
    while N != 0:
        v = N % 10
        N = N // 10
        total += v

    return total
    # return N + sum(map(int, list(str(N))))

for i in range(1, 10001):
    flag = False

    for j in range(1, i):
        if d(j) == i:
            flag = True
            break

    if flag == False:
        print(i)