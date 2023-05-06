def solution(lottos, win_nums):
    answer = 7
    for i in lottos:
        if i in win_nums:
            answer -= 1
    return [min(6,answer-lottos.count(0)), min(6,answer)]