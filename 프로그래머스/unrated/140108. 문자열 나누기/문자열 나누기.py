def solution(s):
    equal, notEqual, answer = 0, 0, 0
    for i in s:
        if equal==notEqual:
            answer+=1
            a=i
        if i==a:
            equal += 1
        else:
            notEqual += 1
    return answer