def solution(n, left, right):
    answer = []
    for row in range(left//n+1, right//n+2):
        answer += [row if col <= row else col for col in range(1, n+1)]
    new_left = left%n
    new_right = (right//n-left//n)*n+right%n
    return answer[new_left:new_right+1]