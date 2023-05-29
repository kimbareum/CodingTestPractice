def solution(storey):
    answer = 0
    c = 10
    while storey*10 >= c:
        curr = (storey%c)//(c//10)
        if curr == 5 and (storey%(c*10))//c >= 5:
            answer += 5
            storey += 5*(c//10)
        elif curr <= 5:
            answer += curr
            storey -= curr*(c//10)
        else:
            answer += (10-curr)
            storey += (10-curr)*(c//10)
        c *= 10
    return answer