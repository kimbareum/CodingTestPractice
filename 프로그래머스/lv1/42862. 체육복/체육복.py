def solution(n, lost, reserve):
    reserve = set(reserve)
    lost = set(lost)
    lost, reserve = lost - reserve, reserve - lost
    reserved = set()
    answer = n-len(lost)
    for i in lost:
        if i-1 not in reserved and i-1 in reserve:
            answer += 1
            reserved.add(i-1)
        elif i+1 not in reserved and i+1 in reserve:
            answer += 1
            reserved.add(i+1)
    return answer
