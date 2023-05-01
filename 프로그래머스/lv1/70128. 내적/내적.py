def solution(a, b):
    #return sum(map(lambda x,y:x*y,a,b))
    answer = 0
    for x,y in zip(a,b):
        answer+=x*y
    return answer
