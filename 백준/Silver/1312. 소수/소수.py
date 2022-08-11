'''
분자와 분모가 있음 각각 A,B
두 수를 나눴을 떄 소수점 아래 N번쨰 자리수를 구하려고 함
'''


A, B, N = map(int, input().split())

A %= B
for _ in range(N):
  A *= 10
  answer = int(A / B)
  A %= B

print(answer)