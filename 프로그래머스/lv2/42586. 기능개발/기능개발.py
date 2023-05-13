import math

def solution(progresses, speeds):
    left_days = [math.ceil((100-progress)/speed) for progress, speed in zip(progresses,speeds)]
    # -((progress-100)//speed) math.ceil 없이 올림하기
    answer = [0]
    left_day = left_days[0]
    for day in left_days:
        if left_day >= day:
            answer[-1] += 1
        else:
            answer.append(1)
            left_day = day
    return answer
