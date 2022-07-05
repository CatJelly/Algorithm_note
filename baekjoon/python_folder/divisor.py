# https://www.acmicpc.net/problem/1037

# 1. 약수 구하는 방법으로 모든 경우를 만족하는 수 찾기  ### 실패..
# 2. 약수니까 제곱근 숫자 중 조합으로 원래 숫자 구하기
# 3. 어떤 수 / 어떤 수의 약수중 최소 = 어떤 수의 약수중 최대  ### 정답

N = int(input())
# div_list = list(int(x) for x in input().split())
div_list = list(map(int, input().split()))
max_n = max(div_list)
min_n = min(div_list)

print(max_n * min_n)

# N = max_n + 1
# while True:
#     flag = True
#     for n in div_list:
#         if N % n != 0:
#             flag = False
#             N += 1
#             break

#     if flag == True:
#         break;

# print(N)
