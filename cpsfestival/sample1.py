# 다리 건너기
# 다리를 건너는 인원의 능력치 = [1,2,5,10]
# 2 + 1 + 10 + 2 + 2
# 1. 먼저 빠른 사람 2명이 갔다옴
# 2. 제일 빠른 사람이 횟불 전달때문에 복귀
# 3. 제일 느린 2명을 같이 보냄
# 4. 건너간 사람중 젤 빠른 사람이 횟불 전달때문에 복귀
# 5. 마지막 남은 2명이 건넘

def crossing(before, after):
    cross_member = []
    if after == []:
        cross_member.append(before.pop())
        cross_member.append(before.pop())
    else:
        before.reverse()
        cross_member.append(before.pop())
        cross_member.append(before.pop())
    
    for member in cross_member:
        after.append(member)
    
    return max(cross_member)

def crossing_reverse(before, after):
    crossing_member = 0
    if before == []:
        return 0
    else:
        crossing_member = after.pop()
        before.append(crossing_member)
        return crossing_member


before = [1,2,5,10]
after = []
light = True # True : before / False : after
total = 0

while before != []:
    #if light:
    total += crossing(before, after)
    before.sort()
    after.sort()
    total += crossing_reverse(before, after)
    before.sort()
    after.sort()

print(total)




