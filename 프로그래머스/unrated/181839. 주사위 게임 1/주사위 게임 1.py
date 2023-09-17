def solution(a, b):
    flag = a%2 + b%2
    if flag == 2:
        return a**2 + b**2
    if flag == 1:
        return 2 * (a + b)
    if flag == 0:
        return abs(a - b)