# https://www.acmicpc.net/problem/1193

#  1      2      3      4      5      X번째 분수 찾기
# 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> ...
# 규칙 => 분모 1인 경우 역수로 뒤집음
#     => 분자 1인 경우 분자 +1 분모 -1
#     => 위 경우를 반복하며 진행시 인덱스 1씩 해당

# 1/1 1/2 2/1 3/1 2/2 3/1 1/4 2/3 3/2 4/1 1/5 2/4 3/3 4/2 5/1

def act1(num, deno, mode):
    if mode == True: 
        return num+1, deno
    else:
        return num, deno+1

def act2(num, deno, mode):
    if mode == True: 
        return num-1, deno+1
    else:
        return num+1, deno-1

X = int(input())
num, deno = 1, 1

i = 1
act_flag = 0
up_down = False
while True:
    if i == X:
        break
    elif (deno == 1 or num == 1) and act_flag == 0:
        act_flag = 1

    if act_flag == 1:
        num, deno = act1(num, deno, up_down)
        act_flag = -1
    else:
        num, deno = act2(num, deno, up_down)
        act_flag = -1
        if deno == 1 or num == 1:
            act_flag = 0
            up_down = not up_down 

    i += 1


print(f'{num}/{deno}')

'''
입력된 값 X에 따라서 X번째의 위치를 파악하기 위해
해당 패턴을 분석하면 사선으로 각 줄을 나눠서 분류했을 때
 1      2           3              4
[1/1], [1/2, 2/1], [3/1,2/2,1/3], [1/4,2/3/,3/2,4/1] ...
다음과 같은 숫자 배열인데 패턴을 찾아보면
홀수 번째 사선, 짝수 번째 사선 일때 각각에 따라서 
분자 = line-gap or 1+gap
분모 = 1+gap or line-gap
임..

몇번째 라인인지를 찾으려면 X번째가 line의 몇번째에 포함되는지를 찾으면 됨

아래는 해당 내용을 코드화 한것
'''

input_num = int(input())

line = 0  # 사선 라인
max_num = 0  # 입력된 숫자(input_num 변수)의 라인에서 가장 큰 숫자
while input_num > max_num:
    line += 1  
    max_num += line  

gap = max_num - input_num 
if line % 2 == 0:  # 사선 라인이 짝수번째 일 때
    top = line - gap  #분자
    under = gap + 1  #분모
else :  # 사선 라인이 홀수번째 일 때
    top = gap + 1  #분자
    under = line - gap  #분모
print(f'{top}/{under}')
