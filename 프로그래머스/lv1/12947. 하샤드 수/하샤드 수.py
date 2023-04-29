def solution(x):
    suma = sum([int(i) for i in str(x)])
    return True if x%suma == 0 else False