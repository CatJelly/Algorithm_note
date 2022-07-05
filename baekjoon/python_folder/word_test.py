# https://www.acmicpc.net/problem/1157

# 전체 문자열 탐색해 알파벳 카운트
# 해시맵 활용

str_list = list(input())
word_dict = {}

for ch in str_list:
    ch = ch.upper()
    if word_dict.get(ch) != None:
        word_dict[ch] += 1
    else:
        word_dict[ch] = 1

max_key = ''
max_value = -1
cnt = 0

for key in word_dict.keys():
    if word_dict[key] > max_value:
        max_key = key
        max_value = word_dict[key]
        cnt = 1
    elif word_dict[key] == max_value:
        cnt += 1

if cnt == 1:
    print(max_key)
else:
    print("?")
