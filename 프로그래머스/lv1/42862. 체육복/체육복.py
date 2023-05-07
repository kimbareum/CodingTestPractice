def solution(n, lost, reserve):
    reserve = set(reserve)
    lost = set(lost)
    lost, reserve = lost - reserve, reserve - lost
    if len(lost) == 0:
        return n
    reserved = []
    answer = n-len(lost)
    for i in lost:
        if i-1 not in reserved and i-1 in reserve:
            answer += 1
            reserved.append(i-1)
        elif i+1 not in reserved and i+1 in reserve:
            answer += 1
            reserved.append(i+1)
    return answer