def solution(d, budget):
    d.sort(reverse=True)
    answer = 0
    while budget>0 and len(d)>0:
        budget -= d.pop()
        if budget >=0:
            answer +=1
    return answer