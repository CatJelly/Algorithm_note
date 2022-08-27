num_list = list(map(int, input().split()))
min_num = min(num_list)

while True:
    cnt = 0
    for num in num_list:
        if min_num % num == 0:
            cnt += 1
    
    if cnt >= 3:
        break

    min_num += 1

print(min_num)