def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for i, j in enumerate(citations, 1):
        if i <= j:
            answer = i
        else:
            break
    return answer