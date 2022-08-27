N = int(input())
n = N
cycle = 0
res = -1
while res != N:
    temp = int(n / 10) + n % 10
    res = n % 10 * 10 + temp % 10
    n = res
    cycle +=1 

print(cycle)