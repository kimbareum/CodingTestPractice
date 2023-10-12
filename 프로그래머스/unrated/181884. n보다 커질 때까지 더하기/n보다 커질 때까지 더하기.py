def solution(numbers, n):
    sumation = 0
    count = 0
    while sumation <= n:
        sumation += numbers[count]
        count += 1
    return sumation