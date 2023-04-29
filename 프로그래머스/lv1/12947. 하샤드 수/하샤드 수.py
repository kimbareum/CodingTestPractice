def solution(x):
    # suma = sum([int(i) for i in str(x)])
    suma = sum(map(int,list(str(x))))
    return True if x%suma == 0 else False