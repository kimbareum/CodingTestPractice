def solution(answers):
    len_ans = len(answers)
    first = [1, 2, 3, 4, 5]*(len_ans//5+1)
    second = [2, 1, 2, 3, 2, 4, 2, 5]*(len_ans//8+1)
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*(len_ans//10+1)
    score = [0, 0, 0]
    answer = []
    for i, j, k, l in zip(answers,first,second,third):
        if i == j:
            score[0] += 1
        if i == k:
            score[1] += 1
        if i == l:
            score[2] += 1
    maxscore = max(score)
    for i in range(3):
        if score[i] == maxscore:
            answer.append(i+1)
    return answer