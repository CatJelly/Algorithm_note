# https://www.acmicpc.net/problem/1296

key = list(input())
N = int(input())

love = ["L", "O", "V", "E"]
name_list = list(input() for _ in range(N))
name_list.sort()
score_list = []
for name in name_list:
    temp = {}
    for k in love:
        temp[k] = name.count(k) + key.count(k)
    score_list.append(temp)

total_list = []
for score in score_list:
    total = 1
    for i in range(len(love)):
        key1 = love[i]
        for j in range(i+1, len(love)):  
            key2 = love[j]
            total *= (score[key1] + score[key2])
    total_list.append(total % 100)

max_val = max(total_list)
print(name_list[total_list.index(max_val)])