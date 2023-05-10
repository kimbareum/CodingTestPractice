def solution(people, limit):
    thin = sorted([i for i in people if i <= limit//2],reverse=True)
    fat = sorted([i for i in people if i > limit//2])
    answer = 0
    while thin and fat:
        if thin[-1] + fat[-1] <= limit:
            thin.pop()
            fat.pop()
        else:
            fat.pop()
        answer += 1
    return answer + len(thin)//2 + len(thin)%2 + len(fat)