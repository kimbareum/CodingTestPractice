import math

def solution(progresses, speeds):
    left_days = [math.ceil((100-progress)/speed) for progress, speed in zip(progresses,speeds)]
    answer = [0]
    left_day = left_days[0]
    for day in left_days:
        if left_day >= day:
            answer[-1] += 1
        else:
            answer.append(1)
            left_day = day
    return answer