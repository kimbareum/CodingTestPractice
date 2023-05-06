def solution(number, limit, power):
    if number <= 2:
        return 3 if number == 2 else 1
    answer = 3
    for i in range(3, number+1):
        cnt = 0
        for j in range(1, int(i**0.5)+1):
            if j == i**0.5:
                cnt += 1
            elif i%j == 0:
                cnt += 2
            if cnt > limit:
                break
        if cnt <= limit :
            answer += cnt
        else:
            answer += power
    return answer
