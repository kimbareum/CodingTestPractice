def solution(k, m, score):
    if len(score) < m:
        return 0
    answer = 0
    score.sort()
    for i in range(1,len(score)//m+1):
        answer += score[-m*i]*m
    return answer