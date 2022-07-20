'''
크기가 엔인 수열 에이가 주어짐
세준이는 인접한 두 원소의 차이를 이용해
크기가 엔 - 1인 수열 비를 만들수 있음

예를들어

A = [5,6,3,9,-1]
B = [1, -3, 6, -10]
B[i] = A[i+1] - A[i]
수열 A 주고 K번 했을떄 나오는 수열 출력
'''

N, K = map(int, input().split())
A = list(map(int, input().split(',')))

for _ in range(K):
  B = [0 for i in range(len(A) - 1)]
  for i in range(len(A) - 1):
    B[i] = A[i+1] - A[i]
  A = B

for i in range(len(A) - 1):
  print(A[i], end=',')
print(A[-1])