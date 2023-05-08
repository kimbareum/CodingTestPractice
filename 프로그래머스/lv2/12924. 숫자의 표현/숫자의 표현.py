def solution(n):
    answer = 0
    cnt = 1
    while True:
        temp = n//cnt
        if cnt%2 != 0:
            if temp-cnt//2 <= 0:
                break
            if temp*cnt == n:
                answer += 1
        else:
            if temp-cnt//2 < 0:
                break
            if temp*cnt+cnt//2 == n:
                answer += 1
        cnt+=1
    return answer