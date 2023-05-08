def solution(s):
    flag = 1
    answer = ''
    for i in s:
        if i == ' ':
            answer += i
            flag = 1
        else:
            answer += i.lower() if flag == 0 else i.upper()
            flag = 0
    return answer