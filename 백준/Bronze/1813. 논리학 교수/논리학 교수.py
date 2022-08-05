'''
a,b,c는 정수
정확하게 a개의 말은 참이다.
정확하게 b개의 말은 참이다.

n개의 말이 참인 개수가 n개인 것중 최대 찾기
'''

N = int(input())
n_list = list(map(int, input().split()))

true_value = [0] * 51
true_flag = []

for i, n in enumerate(n_list):
  true_value[n] += 1

for i in range(len(true_value)):
  if i == true_value[i]:
    true_flag.append(i)

if true_flag == []:
  print(-1)
else:
  print(max(true_flag))