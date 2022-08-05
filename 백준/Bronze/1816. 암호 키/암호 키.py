'''
암호 시스템 
 => 매우 큰 소수의 곱으로 만들어진 수를 암호키로 이용
어떤 수 S가 주어짐
S가 적절한 암호키인지 아닌지 구하기
S의 모든 소인수가 > 10^6 이면 적절한 암호키
'''

def is_prime_number(number):
  for i in range(2, 10**6 + 1):
    if number % i == 0:
      return False

  return True

N = int(input())

for _ in range(N):
  S = int(input())
  if is_prime_number(S):
    print("YES")
  else:
    print("NO")