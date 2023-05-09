def solution(s):
    q1 = list(s)
    q2 =[q1.pop()]
    while q1:
        now = q1.pop()
        if q2 != [] and now == q2[-1]:
            q2.pop()
        else:
            q2.append(now)
    return 1 if q2 == [] else 0