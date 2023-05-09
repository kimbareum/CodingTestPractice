def solution(brown, yellow):
    for i in range(1, yellow//2+2):
        if (i+2)*2+(yellow/i)*2 == brown:
            return [max(i+2,yellow/i+2),min(i+2,yellow/i+2)]
