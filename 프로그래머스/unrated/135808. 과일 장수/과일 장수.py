def solution(k, m, score):
    if len(score) < m:
        return 0
    
    score.sort()
    # answer = 0
    # for i in range(1,len(score)//m+1):
    #     answer += score[-m*i]*m
    # return answer
    return sum(score[len(score)%m::m])*m