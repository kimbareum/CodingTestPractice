def solution(s):
    s = list(reversed(s))
    answer = 1
    while len(s)>2:
        char = s.pop()
        equal, notEqual = 1, 0 
        while equal != notEqual and len(s) > 0:
            temp = s.pop()
            if char == temp:
                equal += 1
            else:
                notEqual += 1
        if len(s) == 0:
            break
        if equal == notEqual:
            answer += 1
    return answer