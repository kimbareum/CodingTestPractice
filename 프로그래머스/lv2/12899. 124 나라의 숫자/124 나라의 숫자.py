def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        n, rest = divmod(n,3)
        if rest == 0:
            answer = '1'+ answer
        elif rest == 1:
            answer = '2' + answer
        else:
            answer = '4' + answer      
    return answer