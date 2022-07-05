# https://www.acmicpc.net/problem/1145

# 최대 공약수 
# for i in range(min(a,b), 0, -1):
#     if a%i == 0 and b%i == 0:
#         return i

# 최소 공배수 
# for i in range(max(a,b), (a*b) + 1):
#     if i%a == 0 and i % b == 0:
#         return i

# 유클리드 호재법
# def GCD(x,y):
#     while y:
#         x, y = y, x % y
#     return x

# def LCM(x,y):
#     return (x*y) // GCD(x,y)

# 브루트 포스 알고리즘 = 완전 탐색 알고리즘
# - 해가 존재할 것으로 예상되는 모든 영역을 전체 탐색하는 방법
# => 최소값으로부터 값을 1씩 증가시켜 5개 숫자들을 나누었을때
#    나머지가 0인 숫자가 3개 이상이면 반복 중단하도록

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
