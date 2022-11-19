def gcd(A, B):
    while B != 0:
        r = A % B
        A = B
        B = r
    
    return A    

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    print(int(A * B / gcd(A,B)))
