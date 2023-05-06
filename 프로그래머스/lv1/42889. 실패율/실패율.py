# def solution(N, stages):
#     answer = dict()
#     reach = len(stages)
#     for i in range(1,N+1):
#         if reach == 0:
#             answer.update({i : 0})
#         else:
#             answer.update({i : stages.count(i)/reach})
#             reach -= stages.count(i)
#     return sorted(answer, key = answer.get, reverse = True)

# 매번 count 해주는것보단 collections 의 Counter를 사용해서 정리해두면 빠름.

from collections import Counter

def solution(N, stages):
    answer = dict()
    reach = len(stages)
    fail = Counter(stages)
    fail = dict(sorted(list(fail.items())))
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
