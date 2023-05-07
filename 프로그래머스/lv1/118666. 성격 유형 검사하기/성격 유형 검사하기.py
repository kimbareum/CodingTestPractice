def solution(survey, choices):
    case = ["RT","TR","CF","FC","JM","MJ","AN","NA"]
    caseDic = dict(zip(case,
                       [(0,1),(0,-1),(1,1),(1,-1),(2,1),(2,-1),(3,1),(3,-1)]))
    scores = [0 for _ in range(4)]
    for i, j in zip(survey,choices):
        score = j-4
        a, b = caseDic.get(i)
        scores[a] += b*score

    return ''.join([case[i*2][0] if scores[i] <= 0 else case[i*2][1] for i in range(4)])