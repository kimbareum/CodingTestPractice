from collections import Counter

def solution(N, stages):
    answer = dict()
    reach = len(stages)
    fail = Counter(stages)
    for i in range(1,N+1):
        temp = fail.get(i)
        if reach == 0:
            answer.update({i : 0})
        else:
            if temp == None:
                answer.update({i : 0})
            else :
                answer.update({i : temp/reach})
                reach -= temp
    return sorted(answer, key = answer.get, reverse = True)