'''
N으로 나눴을때 나머지와 몫이 같은 모든 자연수의 합을 구하기

위 조건을 만족하려면
N+1부터 N^2까지의 범위이고 N+1의 배수임
'''

N = int(input())
sum = 0
for i in range(N+1, N**2, N+1):
    sum += i

print(sum)