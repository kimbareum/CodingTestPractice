def solution(want, number, discount):
    want2 = []
    for i, j in zip(want, number):
        want2 += [i for _ in range(j)]
    want2.sort()
    answer = 0
    for i in range(len(discount)-9):
        if want2 == sorted(discount[i:i+10]):
            answer += 1
    return answer