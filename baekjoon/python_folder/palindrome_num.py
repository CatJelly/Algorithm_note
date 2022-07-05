# https://www.acmicpc.net/problem/1259

while True:
    num = str(input())

    if num == '0':
        break

    while len(num) > 1:
        if num[0] == num[-1]:
            num = num[1:-1]
        else:
            break
    
    if len(num) <= 1:
        print("yes")
    else:
        print("no")