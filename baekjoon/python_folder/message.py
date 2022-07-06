# https://www.acmicpc.net/problem/1384

# 원형으로 아이들이 둘러 앉음
# 종이 위 자신의 이름을 적음
# 각자 종이를 왼쪽으로 전달
# 받은 종이에 칭찬을 쓰기 (긍정 = P, 부정 = N)
# (자기 이름이 나올 떄까지 반복)
# 부정 적은 사람 찾기

def print_bad_person(name_from, name_to):
    print(f'{name_from} was nasty about {name_to}')


i = 1
N = -1

while True:
    people = list()
    nasty = list()
    N = int(input())
    if N == 0:
        break
    
    for _ in range(N):
        temp = input()
        people.append(temp.split())

    for p_index, person in enumerate(people):
        idx = list()
        if 'N' in person:
            for j in range(len(person)):
                if person[j] == 'N':
                    idx.append(j)

        if len(idx) != 0:
            for j in range(len(idx)):
                p = people[abs(N - idx[j] + p_index) % N]
                nasty.append([p[0], person[0]])
            

    print(f"Group {i}")
    if len(nasty) == 0:
        print("Nobody was nasty")

    for n in nasty:
        print_bad_person(n[0], n[1])
    print()
    
    i += 1
