def solution(n):
    if n <= 3:
        return n
    prev1 = 2
    prev2 = 1
    answer = 0
    for i in range(3,n+1):
        answer = prev1 + prev2
        prev1, prev2 = answer, prev1
    return answer%1234567