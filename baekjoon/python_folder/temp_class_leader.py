# https://www.acmicpc.net/problem/1268

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
set_list = [set() for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(5):
            if i == j:
                break
            if table[i][k] == table[j][k]:
                set_list[i].add(j)

# temp = -1
# for i, s in enumerate(set_list):
#     if len(s) > temp:
#         leader = i + 1
#         temp = len(s)

# print(leader)

cnt_list = list(map(lambda x : len(x), set_list))
print(cnt_list.index(max(cnt_list)) + 1)