def solution(myString, pat):
    pat = pat.replace('A', 'X').replace('B', 'A').replace('X', 'B')
    return 1 if pat in myString else 0