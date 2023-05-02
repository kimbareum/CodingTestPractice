def solution(a, b):
    big, small = max(a, b), min(a, b)
    # c,d = max(a, b), min(a, b)
    t = 1
    while t>0:
        t = big%small
        big, small = small, t
    answer = [big, int(a*b/big)]
    return answer