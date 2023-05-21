def solution(n):
    answer = ''
    while n >= 1:
        n, rest = divmod(n,3)
        if rest == 0:
            answer = '4'+ answer
            n -= 1
        elif rest == 1:
            answer = '1' + answer
        else:
            answer = '2' + answer      
    return answer