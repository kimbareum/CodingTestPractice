def solution(n):
    curr = 0
    next = 1
    for i in range(1, n):
        curr, next = next, curr + next

    return next%1234567