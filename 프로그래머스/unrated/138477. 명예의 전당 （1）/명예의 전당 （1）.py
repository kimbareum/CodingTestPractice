from collections import deque

def solution(k, score):
    if len(score) <= k:
        return [min(score[0:i+1]) for i in range(len(score))]
    best = [score[i] for i in range(k)]
    answer = [min(best[0:i+1]) for i in range(k)]
    for i in score[k:]:
        if i >= min(best):
            best[best.index(min(best))] = i
        answer.append(min(best))
    return answer