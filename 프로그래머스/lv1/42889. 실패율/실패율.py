def solution(N, stages):
    answer = dict()
    reach = len(stages)
    for i in range(1,N+1):
        if reach == 0:
            answer.update({i : 0})
        else:
            answer.update({i : stages.count(i)/reach})
            reach -= stages.count(i)
    return sorted(answer, key = answer.get, reverse = True)