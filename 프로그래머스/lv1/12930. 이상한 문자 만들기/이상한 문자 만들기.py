def solution(s):
    s = list(s)
    answer = []
    index = 0
    for i in s:
        if i == ' ':
            index = 0
            answer.append(i)
            continue
        if index%2 == 0:
            answer.append(i.upper())
            index += 1
        else :
            answer.append(i.lower())
            index += 1
    return ''.join(answer)