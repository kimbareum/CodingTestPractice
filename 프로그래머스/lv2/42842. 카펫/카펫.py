def solution(brown, yellow):
    for i in range(1, yellow//2+2):
        if (i+2)*2+(yellow/i)*2 == brown:
            return [i+2,yellow/i+2] if i+2>yellow/i+2 else [yellow/i+2,i+2]