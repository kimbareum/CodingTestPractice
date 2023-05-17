def solution(n):
    one = 1
    two = 2
    for i in range(2,n):
        one, two = two, (one+two)%1000000007
    return two