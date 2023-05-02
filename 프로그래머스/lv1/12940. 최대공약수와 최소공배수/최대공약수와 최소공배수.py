def solution(n, m):
    answer = [0,0]
    big = max(m,n)
    small = min(m,n)
    for i in range(small,0,-1):
        if big % i == 0 and small % i == 0:
            answer[0] = i
            answer[1] = (small*big)//answer[0]
            break
    
    return answer