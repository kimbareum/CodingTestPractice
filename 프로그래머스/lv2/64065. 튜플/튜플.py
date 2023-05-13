import re

def solution(s):
    p = re.compile('\{([^}|^{]+)')
    s = p.findall(s)
    s = sorted(s, key = len)
    answer = []
    for set_1 in s:
        set_1 = set_1.split(',')
        answer += [int(i) for i in set_1 if int(i) not in answer]
    return answer
    