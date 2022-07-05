# https://www.acmicpc.net/problem/1032

# 겹쳐지는 문자 를 찾아내기 
# 겹쳐지는 부분을 제외하고는 ?로 처리

command = []

N = int(input())

str_list = []
for i in range(N):
    str_list.append(input())

for i in range(len(str_list[0])):
    # flag = False
    command.append(str_list[0][i])
    for str in str_list:
        if command[i] != str[i]:
            command[i] = '?'
            break
    # if flag == True:
    #     command[i] = '?'
        

# print(''.join(s for s in command))
print(''.join(command))
