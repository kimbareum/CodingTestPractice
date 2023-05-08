def solution(s):
    answer = 0
    for i in s:
        answer += 1 if i == '(' else -1
        if answer < 0:
            return False
    return True if answer == 0 else False