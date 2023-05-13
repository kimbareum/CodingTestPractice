def solution(n, left, right):
    answer = []
    for i in range(left//n+1, right//n+2):
        answer += [i if j <= i else j for j in range(1, n+1)]
    return answer[left%n:(right//n-left//n)*n+right%n+1]