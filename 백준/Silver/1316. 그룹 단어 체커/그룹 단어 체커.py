'''
그룹 단어 = 단어에 존재하는 모든 문자에 대해
각 문자가 연속해서 나타나는 경우
ex) ccazzzzbb, kin은 그룹 단어
    aabbbccbb는 그룹 단어 아님
'''

N = int(input())
answer = N

for _ in range(N):
    word_cnt = [0] * 26
    char_flag = [False] * 26
    word = input()

    ch = word[0]
    index = ord(ch) - ord('a')
    word_cnt[index] += 1
    char_flag[index] = True
    curr_char = ch
    for i in range(1, len(word)):
        ch = word[i]
        index = ord(ch) - ord('a')
        if curr_char != ch and word_cnt[index] != 0 and char_flag[index] != False:
            answer -= 1
            break
        word_cnt[index] += 1
        char_flag[index] = True
        curr_char = ch

print(answer)
