def solution(n):
    if n <= 3:
        return n
    prev1 = 3
    prev2 = 2
    for i in range(4,n+1):
        prev1, prev2 = prev1 + prev2, prev1
    return prev1%1234567